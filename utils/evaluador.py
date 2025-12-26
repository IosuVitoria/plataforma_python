import io
import sys

def evaluar(codigo, salida_esperada):
    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        exec(codigo)
        sys.stdout = sys.__stdout__
        return buffer.getvalue().strip() == salida_esperada, buffer.getvalue()
    except Exception as e:
        sys.stdout = sys.__stdout__
        return False, str(e)
