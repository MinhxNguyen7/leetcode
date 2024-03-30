from functools import reduce
from itertools import chain, repeat
from typing import Any, Callable, Iterable, NamedTuple

class TestResults(NamedTuple):
    passed: int
    out_of: int
    
    def __add__(self, other: "TestResults|bool") -> "TestResults":
        if isinstance(other, bool):
            return TestResults(
                self.passed + 1,
                self.out_of + 1
            )
            
        if isinstance(other, TestResults):
            return TestResults(
                self.passed + other.passed,
                self.out_of + other.out_of
            )
            
        raise TypeError(f"TestResults.__add__: Expected TestRests or bool, got {type(other)}")
    
    @staticmethod
    def zero():
        return TestResults(0, 0)

def test(expected: Any, func: Callable, *args, **kwargs) -> TestResults:
    res = func(*args, **kwargs)
    success = expected == res
    
    arguments = ', '.join(chain(
        (str(arg) for arg in args),
        (f"{key}={value}" for key, value in kwargs)
    ))
    
    print(
        f"{func.__name__}({arguments})",
        "(PASSED)" if success else "(FAILED)", 
        f"Expected {expected}, Got {res}",
    )
    
    return TestResults(success, 1)
    
    
def run_tests(
    expected_values: Iterable[Any], 
    func: Callable, 
    arguments: Iterable[Iterable[Any]]|None = None, 
    keyword_args: Iterable[dict[str, Any]]|None = None,
) -> TestResults:
    return reduce(
        lambda x, y: x + y,
        (
            test(expected, func, *args, **kwargs)
            for expected, args, kwargs
            in zip(
                expected_values, 
                arguments if arguments else repeat(()), 
                keyword_args if keyword_args else repeat({})
            )
        ),
        TestResults.zero()
    )