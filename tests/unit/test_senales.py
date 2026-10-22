import numpy as np
import pytest

from psi_lab.senales import cuadrada, espectro, senoidal


def test_numero_de_muestras():
    t, x = senoidal(f=5, fs=100, duracion=2)
    assert t.size == x.size == 999


@pytest.mark.parametrize("f", [10.0, 50.0, 120.0])
def test_pico_en_la_frecuencia_correcta(f):
    _, x = senoidal(f=f, fs=1000, duracion=1)
    freqs, amp = espectro(x, fs=1000)
    assert freqs[np.argmax(amp)] == pytest.approx(f)


def test_amplitud_recuperada():
    _, x = senoidal(f=50, fs=1000, duracion=1, amplitud=3.0)
    _, amp = espectro(x, fs=1000)
    assert amp.max() == pytest.approx(3.0, rel=1e-6)


def test_espectro_onda_cuadrada_armonicos_impares():
    f, fs = 10.0, 1000.0
    _, x = cuadrada(f=f, fs=fs, duracion=1.0)
    freqs, amp = espectro(x, fs=fs)

    # Verifica picos en armonicos impares: f, 3f, 5f
    for k in [1, 3, 5]:
        idx = np.argmin(np.abs(freqs - k * f))
        assert amp[idx] > 0.2

    # Verifica ausencia de picos en armonicos pares: 2f, 4f, 6f
    for k in [2, 4, 6]:
        idx = np.argmin(np.abs(freqs - k * f))
        assert amp[idx] == pytest.approx(0.0, abs=1e-2)
