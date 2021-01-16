import asyncio
import time
from ..util.stop_watch import stop_watch


async def sleep(duration: int, result_list: list):
    for _ in range(duration):
        await asyncio.sleep(0)
    result_list.append(duration)


@stop_watch
def sort(input_list: list) -> list:
    result_list = []

    loop = asyncio.get_event_loop()
    loop_was_not_running = not loop.is_running()

    def wait_sorting(future):
        if loop_was_not_running:
            loop.stop()

    coroutines = [sleep(item, result_list) for item in input_list]
    future = asyncio.gather(*coroutines)
    asyncio.ensure_future(future)
    future.add_done_callback(wait_sorting)

    if loop_was_not_running:
        loop.run_forever()

    return result_list

# def sleep(future, duration: int) -> None:
#     time.sleep(duration)
#     future.set_result(None)
#     return


# def sort(input_list: list) -> list:
#     result_list = []
#     for item in input_list:
#         future = asyncio.futures.Future()
#         sleep(future, item)

#         if future.done():
#             result_list.append(item)

#     return result_list
