/* ptexample.c */

/* Dołączanie nagłówka innego modułu */
#include "pysample.h"

/* Funkcja rozszerzenia używająca eksportowanego interfejsu API */
static PyObject *print_point(PyObject *self, PyObject *args) {
  PyObject *obj;
  Point *p;
  if (!PyArg_ParseTuple(args,"O", &obj)) {
    return NULL;
  }

  /* Uwaga: funkcja zdefiniowana w innym module */
  p = PyPoint_AsPoint(obj);
  if (!p) {
    return NULL;
  }
  printf("%f %f\n", p->x, p->y);
  return Py_BuildValue("");
}

static PyMethodDef PtExampleMethods[] = {
  {"print_point", print_point, METH_VARARGS, "Wyświetla punkt"}, 
  { NULL, NULL, 0, NULL}
};

static struct PyModuleDef ptexamplemodule = {
  PyModuleDef_HEAD_INIT,
  "ptexample",           /* Nazwa modułu */
  "A module that imports an API",  /* Łańcuch znaków z dokumentacją (może mieć wartość NULL) */
  -1,                 /* Długość danych ze stanem interpretera lub -1 */
  PtExampleMethods       /* Tablica metod */
};

/* Funkcja inicjująca moduł */
PyMODINIT_FUNC
PyInit_ptexample(void) {
  PyObject *m;

  m = PyModule_Create(&ptexamplemodule);
  if (m == NULL) 
    return NULL;

  /* Importowanie modułu sample i wczytywanie funkcji z jego interfejsu API  */
  if (!import_sample()) {
    return NULL;
  }
  return m;
}
