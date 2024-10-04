import shutil
import subprocess

from behave import given, then, when  # pylint: disable=no-name-in-module

# pylint: disable=function-redefined


@given("we have ppp installed")
def step_impl(context):  # noqa: F811
    assert shutil.which("ppp") is not None


@when("we run ppp")
def step_impl(context):  # noqa: F811
    final_command = ["ppp"]
    completed_process = subprocess.run(
        final_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        #shell=True,
        cwd=context.scenario_test_dir
    )

    print(f"Test dir: ", context.scenario_test_dir)

    context.return_code = completed_process.returncode
    context.stdout = completed_process.stdout.decode("utf-8")
    context.stderr = completed_process.stderr.decode("utf-8")

    print(context.stdout)
    print(context.stderr)

@when("we run ppp run")
def step_impl(context):  # noqa: F811
    final_command = ["ppp", "run"]
    completed_process = subprocess.run(
        final_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        #shell=True,
        cwd=context.scenario_test_dir
    )
    context.return_code = completed_process.returncode
    context.stdout = completed_process.stdout.decode("utf-8")
    context.stderr = completed_process.stderr.decode("utf-8")

    print(context.stdout)
    print(context.stderr)


@then('return code is "{return_code}"')
def step_impl(context, return_code):  # noqa: F811
    assert context.return_code == int(return_code)
