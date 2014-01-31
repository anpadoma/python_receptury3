#include <stdio.h>
#include <Python.h>

void print_chars(char *s, int len) {
  int n = 0;
  while (n < len) {
    printf("%2x ", (unsigned char) s[n]);
    n++;
  }
  printf("\n");
}

void print_wchars(wchar_t *s, int len) {
  int n = 0;
  while (n < len) {
    printf("%x ", s[n]);
    n++;
  }
  printf("\n");
}

static PyObject *py_print_chars(PyObject *self, PyObject *args) {
  char *s;
  Py_ssize_t  len;

  if (!PyArg_ParseTuple(args, "s#", &s, &len)) {
    return NULL;
  }
  print_chars(s, len);
  Py_RETURN_NONE;
}

static PyObject *py_print_wchars(PyObject *self, PyObject *args) {
  wchar_t *s;
  Py_ssize_t  len;

  if (!PyArg_ParseTuple(args, "u#", &s, &len)) {
    return NULL;
  }
  print_wchars(s,len);
  Py_RETURN_NONE;
}


/* Tablica metod modułu */
static PyMethodDef SampleMethods[] = {
  {"print_chars",  py_print_chars, METH_VARARGS},
  {"print_wchars", py_print_wchars, METH_VARARGS},
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
