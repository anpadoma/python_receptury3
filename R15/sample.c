/* sample.c */
#include <math.h>

/* Oblicza największy wspólny dzielnik */
int gcd(int x, int y) {
    int g = y;
    while (x > 0) {
        g = x;
        x = y % x;
        y = g;
    }
    return g;
}

/* Sprawdza, czy (x0,y0) znajduje się w zbiorze Mandelbrota */
int in_mandel(double x0, double y0, int n) {
  double x=0,y=0,xtemp;
  while (n > 0) {
    xtemp = x*x - y*y + x0;
    y = 2*x*y + y0;
    x = xtemp;
    n -= 1;
    if (x*x + y*y > 4) return 0;
  }
  return 1;
}

/* Dzieli dwie liczby */
int divide(int a, int b, int *remainder) {
  int quot = a / b;
  *remainder = a % b;
  return quot;
}

/* Oblicza średnią z wartości elementów tablicy */
double avg(double *a, int n) {
  int i;
  double total = 0.0;
  for (i = 0; i < n; i++) {
    total += a[i];
  }
  return total / n;
}

/* Struktura danych języka C */
typedef struct Point {
    double x,y;
} Point;

/* Funkcja używająca struktury danych języka C */
double distance(Point *p1, Point *p2) {
   return hypot(p1->x - p2->x, p1->y - p2->y);
}
