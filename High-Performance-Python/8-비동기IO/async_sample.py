import asyncio
import datetime
import time


async def run_command_shell(command):
    process = await asyncio.create_subprocess_shell(
        command, stdout = asyncio.subprocess.PIPE, stderr = asyncio.subprocess.PIPE
    )
    print("Started:", datetime.datetime.now(), command, "(pid = " + str(process.pid) + ")", flush = True)
    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        print("Done:", datetime.datetime.now(), command, "(pid = " + str(process.pid) + ")", flush = True)
    else:
        print("Failed:", datetime.datetime.now(), command, "(pid = " + str(process.pid) + ")", flush = True)

    # result = stdout.decode().strip()
    # return result


async def async_main():
    commands = [
        'python -V', 'python -V', 'python -V', 'python -V', 'python -V', 'python -V', 'python -V',
        'python -V', 'python -V', 'python -V', 'python -V', 'python -V', 'python -V', 'python -V',
        'python -V', 'python -V', 'python -V', 'python -V', 'python -V', 'python -V', 'python -V',
    ]

    tasks = []
    for command in commands:
        task = asyncio.create_task(
            run_command_shell(command)
        )
        tasks.append(task)

    for task in tasks:
        await task


if __name__ == '__main__':
    for i in range(3):
        asyncio.run(async_main())
        # print(i * 20, end = ' ')
        if i != 2:
            time.sleep(20)
            # print('sleep')

"""
https://fredrikaverpil.github.io/2017/06/20/async-and-await-with-subprocesses/
"""