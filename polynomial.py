from typing import Any, Callable, Union

class Polynomial:
    PolynomialLike = Union[int, float, 'Polynomial']

    def __init__(self, f: Callable[[int], float]) -> None:
        self.f = f

    def _to_poly(self, x: PolynomialLike) -> 'Polynomial':
        if isinstance(x, Polynomial):
            return x
        elif isinstance(x, int) or isinstance(x, float):
            y = x # Without this, mypy gets confused.
            return Polynomial(lambda i: y if i == 0 else 0)
        else:
            raise TypeError()

    def at(self, i: int) -> float:
        assert i >= 0
        return self.f(i)

    def __add__(self, rhs: PolynomialLike) -> 'Polynomial':
        p = self._to_poly(rhs)
        return Polynomial(lambda i: self.at(i) + p.at(i))

    def __radd__(self, lhs: PolynomialLike) -> 'Polynomial':
        return self._to_poly(lhs) + self

    def __sub__(self, rhs: PolynomialLike) -> 'Polynomial':
        p = self._to_poly(rhs)
        return Polynomial(lambda i: self.at(i) - p.at(i))

    def __rsub__(self, lhs: PolynomialLike) -> 'Polynomial':
        return self._to_poly(lhs) - self

    def __mul__(self, rhs: Union[PolynomialLike, Any]) -> 'Polynomial':
        p = self._to_poly(rhs)
        def f(n: int) -> float:
            return sum(self.at(i) * p.at(n - i) for i in range(n + 1))
        return Polynomial(f)

    def __rmul__(self, lhs: PolynomialLike) -> 'Polynomial':
        return self._to_poly(lhs) * self

    def __pow__(self, n: int) -> 'Polynomial':
        assert n >= 0
        p = self._to_poly(1)
        for _ in range(n):
            p = p * self
        return p

    def __str__(self):
        def x(i: int) -> str:
            assert i >= 0
            if i == 0:
                return ""
            elif i == 1:
                return "x"
            else:
                return f"x^{i}"

        def sign(x: float) -> str:
            return "+" if x >= 0 else "-"

        s = str(self.at(0))
        for i in range(1, 10):
            s += f" {sign(self.at(i))} {abs(self.at(i))}{x(i)}"
        s += " + ..."
        return s

    def __repr__(self):
        return str(self)

x = Polynomial(lambda i: 1 if i == 1 else 0)

def main() -> None:
    p = x**2 + x + 1
    for a in range(0, 3):
        for b in range(0, 3):
            for c in range(0, 3):
                for d in range(0, 3):
                    q = a + b*x + c*x**3 + d*x**4
                    print(f"({p})({q}) = {p * q}")

if __name__ == "__main__":
    main()
