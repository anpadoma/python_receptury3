#include "Python.h"

static PyObject *py_consume_iterable(PyObject *self, PyObject *args) {
  PyObject *obj;
  PyObject *iter;
  PyObject *item;

  if (!PyArg_ParseTuple(args, "O", &obj)) {
    return NULL;
  }
  if ((iter = PyObject_GetIter(obj)) == NULL) {
    return NULL;
  }
  while ((item = PyIter_Next(iter)) != NULL) {
    /* Używanie elementu */
    PyObject_Print(item, stdout, 0);
    printf("\n");
    Py_DECREF(item);
  }
  Py_DECREF(iter);
  return Py_BuildValue("");
}

/* Tablica metod modułu */
static PyMethodDef SampleMethods[] = {
  {"consume_iterable",  py_consume_iterable, METH_VARARGS},
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
