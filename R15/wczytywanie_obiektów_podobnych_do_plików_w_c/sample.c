#include "Python.h"

#define CHUNK_SIZE 8192

/* Pobieranie obiektu podobnego do pliku i wyświetlanie bajtów w strumieniu stdout */
static PyObject *py_consume_file(PyObject *self, PyObject *args) {
  PyObject *obj;
  PyObject *read_meth;
  PyObject *result = NULL;
  PyObject *read_args;

  if (!PyArg_ParseTuple(args,"O", &obj)) {
    return NULL;
  }

  /* Pobieranie metody read przekazanego obiektu */
  if ((read_meth = PyObject_GetAttrString(obj, "read")) == NULL) {
    return NULL;
  }

  /* Tworzenie listy argumentów dla metody read() */
  read_args = Py_BuildValue("(i)", CHUNK_SIZE);
  while (1) {
    PyObject *data;
    PyObject *enc_data;
    char *buf;
    Py_ssize_t len;

    /* Wywołanie metody read() */
    if ((data = PyObject_Call(read_meth, read_args, NULL)) == NULL) {
      goto final;
    }

    /* Wykrywanie końca pliku */
    if (PySequence_Length(data) == 0) {
      Py_DECREF(data);
      break;
    }

    /* Kodowanie znaków Unicode jako bajtów na potrzeby kodu w języku C */
    if ((enc_data = PyUnicode_AsEncodedString(data, "utf-8", "strict")) == NULL) {
      Py_DECREF(data);
      goto final;
    }

    /* Pobieranie danych z bufora */
    PyBytes_AsStringAndSize(enc_data, &buf, &len);

    /* Wyświetlanie w strumieniu stdout (do zastąpienia bardziej użytecznym kodem) */
    write(1, buf, len);

    /* Operacje porządkujące */
    Py_DECREF(enc_data);
    Py_DECREF(data);
  }
  result = Py_BuildValue("");

 final:
  /* Operacje porządkujące */
  Py_DECREF(read_meth);
  Py_DECREF(read_args);
  return result;
}

/* Tablica metod modułu */
static PyMethodDef SampleMethods[] = {
  {"consume_file",  py_consume_file, METH_VARARGS},
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
