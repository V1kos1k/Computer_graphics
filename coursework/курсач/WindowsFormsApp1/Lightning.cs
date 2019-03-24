using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Linq;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using System.Windows;

namespace WindowsFormsApp1
{
    class Lightning
    {
        public List<Point3D[]> Model;
        private Point3D _center;
        public List<Vector[]> segmentList;
        public float xk, yk, zk, x1, y1, z1;
        bool etl_ok = false;
        bool sub_ok = false;

        private ETL etl;
        public Lightning(int h, int w, ETL _etl, int ion, int vol_etl, int vol_sub, Point3D center)
        {
            if (ion != 0)
            {

                etl = _etl;
                _center = new Point3D();
                _center = center;

                // координаты крайних точек молнии
                Rand_start_l(w);

                bool len_lightning_etl_ok;
                bool len_lightning_sub_ok;

                // если ионизация молнии ниже какого-то значения
                // то выбираем рандомную точку 
                // которая не доходит до уровня объектов 
                // и молния заканчивается в воздухе
                int[] length = new int[31]; // массив координаты Y от ионизации
                for (int i = 0; i < 31; i++)  // 1225 / 30
                {
                    if (i < 10)
                        length[i] = i * 10;
                    else if (i < 20)
                        length[i] = i * 15;
                    else
                        length[i] = i * 20;
                }

                // доходит ли молния до объектов
                if (length[ion] >= _etl.S[1].h_rope1[0].Y)
                    len_lightning_etl_ok = true;
                else
                    len_lightning_etl_ok = false;

                if (length[ion] >= _etl.Sub[2].h_rods[0].Y)
                    len_lightning_sub_ok = true;
                else
                    len_lightning_sub_ok = false;

                yk = length[ion];

                // если не доходит, то начать считать молнию до соответствующей точки в воздухе
                if (!len_lightning_etl_ok && !len_lightning_sub_ok)
                {
                    Into_the_sky();
                }

                // если доходит до обоих, то проверить радиус стягивания обоих
                if (len_lightning_etl_ok && len_lightning_sub_ok)
                {
                    bool TRE = Tightening_radius_ETL(_etl);
                    bool TRS = Tightening_radius_SUB(_etl);
                    // если попадает в оба радиуса
                    if (TRE && TRS)
                    {
                        // то сравниваем высоты
                        if (_etl._h_rope > _etl._h_rods)
                            // попадает в ЛЭП
                            Rand_ETL(_etl.S[1].h_rope1[0], _etl.S[1].h_rope2[0]);
                        else if (_etl._h_rope < _etl._h_rods)
                            // попадает в подстанцию
                            Rand_SUB(_etl.Sub);
                        else if (_etl._h_rope == _etl._h_rods)
                            // попадает туда, где напряжение выше
                            Height_comparison(vol_etl, vol_sub, _etl.S[1].h_rope1[0], _etl.S[1].h_rope2[0], _etl.Sub);
                    }
                    // если попадает только в радиус ЛЭП
                    else if (TRE && !TRS)
                        Rand_ETL(_etl.S[1].h_rope1[0], _etl.S[1].h_rope2[0]);
                    // если попадает только в радиус подстанции
                    else if (!TRE && TRS)
                        Rand_SUB(_etl.Sub);
                    // если не попадает в радиусы, ударяет в землю за пределами радиусов
                    else
                        Into_the_ground(x1, z1, _etl.S[2].basis[0], _etl.S[1].basis2[0], _etl._h_rope, _etl.Sub[0].basis, _etl._h_rods);
                }
                // если доходит до ЛЭП, то проветить радиус стягивания ЛЭП
                else if (len_lightning_etl_ok && !len_lightning_sub_ok)
                {
                    if (Tightening_radius_ETL(_etl))
                        Rand_ETL(_etl.S[1].h_rope1[0], _etl.S[1].h_rope2[0]);
                    else
                        Into_the_ground(x1, z1, _etl.S[2].basis[0], _etl.S[1].basis2[0], _etl._h_rope, _etl.Sub[0].basis, _etl._h_rods);
                }
                // если доходит до подстанции, то проверить радиус стягивания подстанции
                else if (!len_lightning_etl_ok && len_lightning_sub_ok)
                {
                    if (Tightening_radius_SUB(_etl))
                        Rand_SUB(_etl.Sub);
                    else
                        Into_the_ground(x1, z1, _etl.S[2].basis[0], _etl.S[1].basis2[0], _etl._h_rope, _etl.Sub[0].basis, _etl._h_rods);
                }
                
                // вычисление ступеней молнии
                Lightning_iteration(ion);
            }
        }

        // начальная точка молнии
        private void Rand_start_l(int w)
        {
            var rand = new Random();
            x1 = rand.Next(0, w);
            y1 = 0;
            z1 = rand.Next(-450, 100);
        }

        // вычисляется рандомная конечная точка молнии в небе
        private void Into_the_sky()
        {
            var rand = new Random();
            xk = rand.Next((int)(x1 - 100), (int)(x1 + 100));
            zk = rand.Next((int)(z1 - 100), (int)(z1 + 100));
            // вызвать функцию, которая высчитывает ступенчатую молнию по координатам крайних точек
        }

        private bool Tightening_radius_ETL(ETL _etl)
        {
            return  x1 > (_etl.S[1].h_rope1[0].X - _etl._h_rope) && (x1 < _etl.S[1].h_rope2[0].X + _etl._h_rope) &&
                    z1 > (_etl.S[1].h_rope1[0].Z - _etl._h_rope) && (z1 < _etl.S[1].h_rope1[0].Z + _etl._h_rope); // должно быть _etl._h_rope*3
        }
        private bool Tightening_radius_SUB(ETL _etl)
        {
            return x1 > _etl.Sub[0].basis[0].X - _etl._h_rods && x1 < _etl.Sub[1].basis[1].X + _etl._h_rods &&
                    z1 > _etl.Sub[2].basis[2].Z - _etl._h_rods && z1 < _etl.Sub[0].basis[0].Z + _etl._h_rods;  // должно быть _etl._h_rods*3
        }

        // высчитывает рандомную точку на троссе, в которую попадет молния
        private void Rand_ETL(Point3D rope1, Point3D rope2)
        {
            var rand = new Random();
            xk = rand.Next((int)(rope1.X), (int)(rope2.X));
            
            zk = rope1.Z;
            if (xk != rope1.X && xk != rope2.X)
                yk = rope1.Y + 10;
            else
                yk = rope1.Y + 5;

            etl_ok = true;
            sub_ok = false;
            // вызвать функцию, которая высчитывает ступенчатую молнию по координатам крайних точек
        }

        // выбирает близжайший стержень, в который попадет молния
        private double D(float x11, float x12, float y11, float y12)
        {
            return Math.Sqrt((x12 - x11) * (x12 - x11) + (y12 - y11) * (y12 - y11));
        }
        private void Rand_SUB(Substation[] sub)
        {
            double[] tmp = new double[4];
            double min = 1000;
            int j = 0;
            for (int i = 0; i < 4; i++)
            {
                tmp[i] = D(x1, sub[i].h_rods[0].X, z1, sub[i].h_rods[0].Z);
                if (tmp[i] < min)
                {
                    j = i;
                    min = tmp[i];
                }
            }
            xk = sub[j].h_rods[0].X;
            yk = sub[j].h_rods[0].Y;
            zk = sub[j].h_rods[0].Z;

            etl_ok = false;
            sub_ok = true;
            // вызвать функцию, которая высчитывает ступенчатую молнию по координатам крайних точек
        }

        // проверяет у какого объекта напряжение выше, и в него ударяет (вызывает одну из функций выше), если одинаковые, то выбирает рандомную
        private void Height_comparison(int vol_etl, int vol_sub, Point3D rope1, Point3D rope2, Substation[] sub)
        {
            if (vol_etl > vol_sub)
                Rand_ETL(rope1, rope2);
            else if (vol_etl < vol_sub)
                Rand_SUB(sub);
            else
            {
                var rand = new Random();
                int tmp = rand.Next(0, 1);
                if (tmp == 0)
                    Rand_ETL(rope1, rope2);
                else
                    Rand_SUB(sub);
            }
        }

        // высчитывает рандомную точку на земле, в которую попадет молния и которая не принадлежит радиусам стягивания объектов
        private void Into_the_ground(float x, float z, Point3D basis1, Point3D basis2, int _h_rope, Point3D[] basis, int _h_rods)
        {
            var rand = new Random();

            if (x < basis[0].X - _h_rods && z < basis1.Z)
            {
                if ((int)x - 200 < (int)basis[0].X - _h_rope)
                    xk = rand.Next((int)x - 200, (int)basis[0].X - _h_rope);
                else
                    xk = rand.Next((int)basis[0].X - _h_rope, (int)x - 200);
                yk = rand.Next(350, (int)basis1.Y - 30);
                if ((int)z - 250 < (int)basis1.Z - _h_rope)
                    zk = rand.Next((int)z - 250, (int)basis1.Z - _h_rope);
                else
                    zk = rand.Next((int)basis1.Z - _h_rope, (int)z - 250);
            }
            else if (x < basis[0].X - _h_rods && z > basis1.Z)
            {
                xk = rand.Next((int)x - 200, (int)basis[0].X - _h_rope);
                yk = rand.Next(350, (int)basis1.Y + 30);
                zk = rand.Next((int)basis1.Z + _h_rope, (int)z + 250);
            }
            else if (x >= basis2.X + _h_rope && z >= basis[0].Z + _h_rods)
            {
                xk = rand.Next((int)basis2.X, (int)x + 200);
                yk = rand.Next((int)basis[0].Y + 30, 632);
                zk = rand.Next((int)basis[0].Z + _h_rods, (int)z + 250);
            }
            else if (x >= basis2.X && z <= basis[0].Z + _h_rods)
            {
                xk = rand.Next((int)basis2.X, (int)x + 200);
                yk = rand.Next(348, (int)basis[2].Y - 30);
                zk = rand.Next((int)z - 250, (int)basis[2].Z - _h_rods);
            }
            else  // ошибка из-за того, что не все варианты рассмотрены, поэтому при значениях (530; 0; -393) выбирается удар в небо
            // надо исправить!!!!!!!!!!!!!!
            {
                // если молния не доходит до объекта из-за длины, но по координатам она входит в радиус стягивания, поэтому не входит в область описанную выше
                Into_the_sky();
            }
        }

        // функция, которая вычисляет перпендикуляр вектора на расстоянии r 
        private Vector PerpendicularCalculate(Vector a, Vector b, Vector c, double r)
        {
            float k = 1;
            if (a.X < b.X)
                k = -1;
            double x = c.X + k*r * (a.Y - b.Y) / Math.Sqrt(Math.Pow(a.X - b.X, 2) + Math.Pow(a.Y - b.Y, 2));
            double y = c.Y - k*r * (a.X - b.X) / Math.Sqrt(Math.Pow(a.X - b.X, 2) + Math.Pow(a.Y - b.Y, 2));
            return new Vector(x, y);
        }

        // функция, которая вычисляет все точки молнии
        private void Lightning_iteration(int ion)
        {
            var rand = new Random();

            Vector startPoint = new Vector(x1, y1);
            Vector endPoint = new Vector(xk, yk);
            Vector[] tmp = { startPoint, endPoint };
            segmentList = new List<Vector[]>();

            segmentList.Add(tmp); // [координаты начала молнии, координаты конца молнии]
            double offsetAmount = ion*3;  // максимальное смещение вершины молнии
            double iteration = 0;
            if (ion <= 5)
                iteration = 3;  // ion/5  // вроде и без этого нормально
            else if (ion <= 15)
                iteration = 4;
            else 
                iteration = ion/4;  // при ion = 30 умирает и выглядит ужасно


            for (int i = 0; i < iteration; i++)
            {
                int end = segmentList.Count;
                for (int q = 0; q < end; q++)  // проходим по списку сегментов, которые были в начале текущей итерации
                {
                    startPoint = segmentList[q][0];
                    endPoint = segmentList[q][1];


                    Vector midPoint = new Vector((segmentList[q][0].X + segmentList[q][1].X) / 2,
                        (segmentList[q][0].Y + segmentList[q][1].Y) / 2);

                    // сдвигаем midPoint на случайную величину в направлении перпендикуляра
                    double r = (offsetAmount - rand.NextDouble() * 2 * offsetAmount);
                    midPoint = PerpendicularCalculate(segmentList[q][0], segmentList[q][1], midPoint, r);

                    segmentList.Remove(segmentList[q]);  // этот сегмент уже не обязателен

                    // делаем два новых сегмента, из начальной точки к серединеи от середины к конечной
                    segmentList.Add(new Vector[] { startPoint, midPoint });
                    segmentList.Add(new Vector[] { midPoint, endPoint });

                    Vector direction = midPoint - startPoint;  // возможно наоборот из-за направления Oy
                    Vector splitEnd = direction * 0.7 + midPoint;  // в оригинале должен быть еще поворот
                    segmentList.Add(new Vector[] { midPoint, splitEnd });
                    
                    end--;
                    q--;
                }
                offsetAmount /= 2;  // каждый раз уменьшаем в два раза смещение центральной точки по сравнению с предыдущей итерацией
            }

            // из Vector в Point3D
            int count = segmentList.Count;
            
            Vector_Point(count);
        }

        private void Vector_Point(int len)
        {
            Model = new List<Point3D[]>();

            float step = Math.Abs(z1 - zk) / len;

            float z = z1;
            if (z1 < zk)
                for (int i = 0; i < len; i++)
                {
                    Model.Add(new Point3D[] { new Point3D((float)segmentList[i][0].X, (float)segmentList[i][0].Y, z + step),
                        new Point3D((float)segmentList[i][1].X, (float)segmentList[i][1].Y, z + step) });
                    z += step;
                }
            else
                for (int i = 0; i < len; i++)
                {
                    Model.Add(new Point3D[] { new Point3D((float)segmentList[i][0].X, (float)segmentList[i][0].Y, z - step),
                        new Point3D((float)segmentList[i][1].X, (float)segmentList[i][1].Y, z - step) });
                    z -= step;
                }
        }

        public void DrawLightning(Graphics g)
        {
            int len = segmentList.Count;
            

            var segment = new PointF[len][];
            for (int i = 0; i < len; i++)
                segment[i] = new PointF[2];
            
            for (int i = 0; i < len; i++)
            {
                segment[i][0].X = (float)Model[i][0].X;
                segment[i][0].Y = (float)Model[i][0].Y;
                segment[i][1].X = (float)Model[i][1].X;
                segment[i][1].Y = (float)Model[i][1].Y;
            }
            
            for (int i = 0; i < len; i++)
            {
                g.DrawLines(new Pen(Color.FromArgb(255, Color.White)), segment[i]);
                Draworeol(segment[i][0], segment[i][1], g);
            }

            DrawFlash(g, segment[0][0].X, segment[0][0].Y, segment[len-1][1].Y);
        }

        static public void Draworeol(PointF p1, PointF p2, Graphics g)
        {
            Color c = Color.FromArgb(160, Color.White);
            for (int i = 0; i < 3; i++)
            {
                c = Color.FromArgb(c.A * (9 - i) / 10, c);
                g.DrawLine(new Pen(c), p1.X + 1 + i, p1.Y, p2.X + 1 + i, p2.Y);
                g.DrawLine(new Pen(c), p1.X - 1 - i, p1.Y, p2.X - 1 - i, p2.Y);
            }
        }

        static public void DrawFlash(Graphics g, float x, float y, float yk)
        {
            var path = new GraphicsPath();
            path.AddEllipse(x - 100 - yk / 2, y - 50 - yk / 3, 200 + yk, 100 + yk/2);
            var pthGrBrush = new PathGradientBrush(path) { CenterColor = Color.FromArgb(255, Color.White) };
            Color[] colors = { Color.FromArgb(0, Color.White) };
            pthGrBrush.SurroundColors = colors;
            
            g.FillEllipse(pthGrBrush, x - 100 - yk / 2, y - 50 - yk / 3, 200 + yk, 100 + yk/2);
        }
    }
}
