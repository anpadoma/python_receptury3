// sample.i - Interfejs Swiga
%module sample
%{
#include "sample.h"
%}

/* Modyfikacje */
%extend Point {
    /* Konstruktor obiektów typu Point */
    Point(double x, double y) {
        Point *p = (Point *) malloc(sizeof(Point));
	p->x = x;
	p->y = y;
	return p;
   };
};

/* Odwzorowanie int *remainder na argument wyjściowy */
%include typemaps.i
%apply int *OUTPUT { int * remainder };

/* Odwzorowanie wzorca argumentu (double *a, int n) na tablice */
%typemap(in) (double *a, int n)(Py_buffer view) {
  view.obj = NULL;
  if (PyObject_GetBuffer($input, &view, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {
    SWIG_fail;
  }
  if (strcmp(view.format,"d") != 0) {
    PyErr_SetString(PyExc_TypeError, "Oczekiwano tablic liczb o podwójnej precyzji");
    SWIG_fail;
  }
  $1 = (double *) view.buf;
  $2 = view.len / sizeof(double);
}

%typemap(freearg) (double *a, int n) {
  if (view$argnum.obj) {
    PyBuffer_Release(&view$argnum);
  }
}

/* Deklaracje kodu w języku C umieszczane w module rozszerzenia */

extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int *remainder);
extern double avg(double *a, int n);  

typedef struct Point {
    double x,y;
} Point;

extern double distance(Point *p1, Point *p2);
