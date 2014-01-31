#include "Python.h"
#include "sample.h"

/* Wywołanie double avg(double *, int) */
static PyObject *py_avg(PyObject *self, PyObject *args) {
  PyObject *bufobj;
  Py_buffer view;
  double result;
  /* Pobieranie przekazanego obiektu Pythona */
  if (!PyArg_ParseTuple(args, "O", &bufobj)) {
    return NULL;
  }

  /* Próba pobrania informacji o buforze z tego obiektu */
  if (PyObject_GetBuffer(bufobj, &view, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {
    return NULL;
  }

  if (view.ndim != 1) {
    PyErr_SetString(PyExc_TypeError, "Oczekiwano jednowymiarowej tablicy");
    PyBuffer_Release(&view);
    return NULL;
  }

  /* Sprawdzanie typu elementów tablicy */
  if (strcmp(view.format,"d") != 0) {
    PyErr_SetString(PyExc_TypeError, "Oczekiwano tablicy liczb o podwójnej precyzji");
    PyBuffer_Release(&view);
    return NULL;
  }

  /* Przekazywanie nieprzetworzonego bufora i rozmiaru do funkcji w języku C */
  result = avg(view.buf, view.shape[0]);

  /* Informowanie, że zakończono używanie bufora */
  PyBuffer_Release(&view);
  return Py_BuildValue("d", result);
}

/* Tablica metod modułu */
static PyMethodDef SampleMethods[] = {
  {"avg",  py_avg, METH_VARARGS, "Średnia"},
  { NULL, NULL, 0, NULL}
};

/* Strutura modułu */
static struct PyModuleDef samplemodule = {
  PyModuleDef_HEAD_INIT,
  "sample",           /* Nazwa modułu */
  "A sample module",  /* Łańcuch znaków z dokumentacją (może mieć wartość NULL) */
  -1,                 /* Długość danych na stan dla interpretera lub -1 */
  SampleMethods       /* Tablica metod */
};

/* Funkcja inicjująca moduł */
PyMODINIT_FUNC
PyInit_sample(void) {
  return PyModule_Create(&samplemodule);
}
