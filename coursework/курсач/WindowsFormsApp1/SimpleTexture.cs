using System.Drawing;

namespace WindowsFormsApp1
{
    class SimpleTexture: Texture
    {
        public SimpleTexture(TextureType textureType, Point p1, Point p2)
        {
            Ttype = textureType;
            _region = new Rectangle(p1.X, p1.Y, p2.X - p1.X, p2.Y - p1.Y);
            switch (Ttype)
            {
                case TextureType.Sky:
                    TBrush = new TextureBrush(Image.FromFile(@"\\Mac\Home\Desktop\Смерть моя\курсач\WindowsFormsApp1\2.jpg", true));
                    TBrush.ScaleTransform(0.7F, 0.7F);   
                    break;
                case TextureType.Ground:
                    TBrush = new TextureBrush(Image.FromFile(@"\\Mac\Home\Desktop\Смерть моя\курсач\WindowsFormsApp1\1.jpg", true));
                    TBrush.ScaleTransform(0.02F, 0.02F);
                    break;
            }
        }
        public void DrawTexture(Graphics g, int angle)
        {
            TBrush.TranslateTransform(-4*angle, 0);
            g.FillRectangle(TBrush, _region);
            TBrush.TranslateTransform(4*angle, 0);
        }

        private readonly Rectangle _region;
    }
}
