/// This function was originally written by Ian Stephenson
displacement doDisplace(float disp = 0.25; float atten = 0.5)
{
    point PP = transform ("object", P);
    normal sN = normalize(ntransform("object",N));
    float scale;
    float ret=evalparam("disp",scale);
    if(ret<0)
	scale=100;
    P = transform("object","current",PP + sN*scale*atten);
    N = calculatenormal(P);
}
///