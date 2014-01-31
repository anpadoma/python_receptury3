#include <stdio.h>
#include <Python.h>

static PyObject *py_die(PyObject *self, PyObject *args) {
  char *s = 0;

  *s = 'x';
  Py_RETURN_NONE;
}


/* Tablica metod modułu */
static PyMethodDef SampleMethods[] = {
  {"die",  py_die, METH_VARARGS},
  { NULL, NULL, 0, NULL}
};

/* Struktura modułu */
static struct PyModuleDef samplemodule = {
  PyModuleDef_HEAD_INIT,
  "sample",           /* Nazwa modułu */
  "A sample module",  /* Łańcuch znaków z dokumentacją (może mieć wartość NULL) */
  -1,                 /* Długość danych ze stanem dla interpretera lub -1 */
  SampleMethods       /* Tablica metod */
};

/* Funkcja inicjująca moduł */
PyMODINIT_FUNC
PyInit_sample(void) {
  return PyModule_Create(&samplemodule);
}
