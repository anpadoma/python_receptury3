#include <stdio.h>
#include <Python.h>

void print_chars(char *s) {
    while (*s) {
        printf("%2x ", (unsigned char) *s);
        s++;
    }
    printf("\n");
}

static PyObject *py_print_chars(PyObject *self, PyObject *args) {
  char *s;

  if (!PyArg_ParseTuple(args, "y", &s)) {
    return NULL;
  }
  print_chars(s);
  Py_RETURN_NONE;
}

static PyObject *py_print_chars_str(PyObject *self, PyObject *args) {
  char *s;

  if (!PyArg_ParseTuple(args, "s", &s)) {
    return NULL;
  }
  print_chars(s);
  Py_RETURN_NONE;
}

static PyObject *py_print_chars_str_alt(PyObject *self, PyObject *args) {
  PyObject *o, *bytes;
  char *s;

  if (!PyArg_ParseTuple(args, "U", &o)) {
    return NULL;
  }
  bytes = PyUnicode_AsUTF8String(o);
  s = PyBytes_AsString(bytes);
  print_chars(s);
  Py_DECREF(bytes);
  Py_RETURN_NONE;
}


/* Tablica metod modułu */
static PyMethodDef SampleMethods[] = {
  {"print_chars",  py_print_chars, METH_VARARGS},
  {"print_chars_str", py_print_chars_str, METH_VARARGS},
  {"print_chars_str_alt", py_print_chars_str_alt, METH_VARARGS},
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
