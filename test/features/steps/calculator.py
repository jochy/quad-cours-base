from behave import *
from basicmath.basic_math import calculator

@given('A number {a:d} and a number {b:d}')
def step_impl(context, a, b):
    context.a = a
    context.b = b

@when('The calculator adds them')
def step_impl(context):
    context.result = calculator('+', context.a, context.b)

@then('The result is {result:d}')
def step_impl(context, result):
    assert context.result == result