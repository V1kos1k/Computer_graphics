using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using System.Diagnostics;
using System.Threading;

namespace WindowsFormsApp1
{
    public class Scene
    {
        //private Shadow _s; // создать класс Shadow
        private readonly PictureBox _picture;
        private readonly Point3D _center;
        private double _pov1, _pov2;
        public double xd;
        public bool flag;
        readonly Point3D _p = new Point3D();
        private ETL _etl; // создать класс ETL
        private Lightning _light; // создать класс
        private Drawing _drawing;
        public int h_support = 111; // высота опор
        public int h_rope = 151; // высота тросса
        public int distance_support = 100; // расстояние между опорами

        public int width_rods = 50; // ширина подстанции (расстояние между стержнями)
        public int height_rods = 50;  // длина подстанции (расстояние между стержнями)
        public int h_building = 15;  // высота зданий
        public int width_building = 30; // ширина зданий
        public int h_rods = 30; // высота стержней

        public int ion; // ионизация
        public int voltage_etl = 110;
        public int voltage_substation = 110;

        public bool _flag_etl; // защищена ли ЛЭП
        public bool _flag_sub; // защищена ли подстанция

        public Scene(PictureBox pictureBox)
        {
            _picture = new PictureBox();
            _picture = pictureBox;
            _picture.BackColor = Color.Black;
            DrawEath();
            _center = new Point3D(_picture.Width / 2, _picture.Height / 2, 0);
            _etl = new ETL(_picture.Width, _picture.Height, 50, 65, 100, 100, 100, 50, 50, 70,_center, 1);
            _pov1 = 1;
        
        }
        private void DrawSky()
        {
            var bmp = new Bitmap(_picture.Image);
            Graphics gr = Graphics.FromImage(bmp);
            var texture = new SimpleTexture(TextureType.Sky, new Point(0, 0),
                new Point(_picture.Width, _picture.Height / 2 + 30));
            texture.DrawTexture(gr, (int)_pov1);
            _picture.Image = bmp;
        }
        private void DrawEath()
        {
            var bmp1 = new Bitmap(_picture.Width, _picture.Height);
            Graphics g = Graphics.FromImage(bmp1);
            var t = new SimpleTexture(TextureType.Ground, new Point(0, _picture.Height / 2 + 30),
                                      new Point(_picture.Width, _picture.Height));
            t.DrawTexture(g, (int)_pov1);

            _picture.Image = bmp1;
        }
        public void Click()
        {
            _etl = new ETL(_picture.Width, _picture.Height, h_support, h_rope, distance_support, width_rods,
                height_rods, h_building, width_building, h_rods, _center, (int)_pov1);
            
            // если защищает - продолжить
            if (_etl._flag_etl && _etl._flag_sub)
            {
                _flag_etl = true;
                _flag_sub = true;
                _light = new Lightning(_picture.Width, _picture.Height, _etl, ion, voltage_etl, voltage_substation, _center);
            }
            else if (!_etl._flag_etl && _etl._flag_sub)
            {
                _flag_etl = false;
                _flag_sub = true;
            }
            else if (_etl._flag_etl && !_etl._flag_sub)
            {
                _flag_etl = true;
                _flag_sub = false;
            }
            else
            {
                _flag_etl = false;
                _flag_sub = false;
            }
            DrawScene();
        }
        private void DrawScene()
        {
            DrawEath();
            DrawSky();

            Stopwatch stopWatch = new Stopwatch();
            stopWatch.Start();
            _drawing = new Drawing(_center, _etl, _light, _picture, ion);
            stopWatch.Stop();
            long ts = stopWatch.ElapsedTicks;
        }
    }
}