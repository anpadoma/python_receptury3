#include <Python.h>

/* Wywołuje func(x,y) w interpreterze Pythona.  Argumenty
   i zwracana wartość funkcji muszą być liczbami
   zmiennoprzecinkowymi z Pythona */

double call_func(PyObject *func, double x, double y) {
  PyObject *args;
  PyObject *kwargs;
  PyObject *result = 0;
  double retval;

  /* Trzeba się upewnić, że zajęto blokadę GIL */
  PyGILState_STATE state = PyGILState_Ensure();
  
  /* Sprawdzanie, czy func to poprawna jednostka wywoływalna */
  if (!PyCallable_Check(func)) {
    fprintf(stderr,"call_func: oczekiwano jednostki wywoływalnej\n");
    goto fail;
  }
  /* Tworzenie argumentów */
  args = Py_BuildValue("(dd)", x, y);
  kwargs = NULL;

  /* Wywoływanie funkcji */
  result = PyObject_Call(func, args, kwargs);
  Py_DECREF(args);
  Py_XDECREF(kwargs);

  /* Sprawdzanie wyjątków z Pythona */  
  if (PyErr_Occurred()) {
    PyErr_Print();
    goto fail;
  }

  /* Sprawdzanie, czy wynik to liczba zmiennoprzecinkowa */
  if (!PyFloat_Check(result)) {
    fprintf(stderr,"call_func: jednostka wywoływalna nie zwróciła liczby zmiennoprzecinkowej\n");
    goto fail;
  }

  /* Tworzenie zwracanej wartości */
  retval = PyFloat_AsDouble(result);
  Py_DECREF(result);

  /* Przywracanie stanu blokady GIL i zwracanie wartości */
  PyGILState_Release(state);
  return retval;

fail:
  Py_XDECREF(result);
  PyGILState_Release(state);
  abort();
}


/* Wczytywanie symbolu z modułu */
PyObject *import_name(const char *modname, const char *symbol) {
  PyObject *u_name, *module;
  u_name = PyUnicode_FromString(modname);
  module = PyImport_Import(u_name);
  Py_DECREF(u_name);
  return PyObject_GetAttrString(module, symbol);
}

/* Prosty przykład osadzania kodu */
int main() {
  PyObject *pow_func;
  double x;

  Py_Initialize();
  /* Pobieranie referencji do funkcji math.pow */
  pow_func = import_name("math","pow");

  /* Uruchamianie funkcji za pomocą wywołania call_func() */
  for (x = 0.0; x < 10.0; x += 0.1) {
    printf("%0.2f %0.2f\n", x, call_func(pow_func,x,2.0));
  }
  /* Gotowe */
  Py_DECREF(pow_func);
  Py_Finalize();
  return 0;
}

