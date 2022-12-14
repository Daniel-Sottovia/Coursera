import aula03
import pytest

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return aula03.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = aula03.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = aula03.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def test_bolha_curta_alet(self, o, l_aleat):
        o.bolha_curta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_selecao_direta_aleat(self, o, l_aleat):
        o.selecao_direta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_bolha_curta_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_direta_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)


