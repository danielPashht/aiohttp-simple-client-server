import asyncio

from aiohttp import web


tasks = {}  # In-memory storage
task_counter = 0
lock = asyncio.Lock()


async def get_tasks(request):
	global tasks
	try:
		if tasks:
			return web.json_response(tasks)
		return web.json_response(
			{'message': 'No tasks found'},
			status=404
		)
	except Exception as e:
		print(f"Internal Server Error: {e}")
		return web.json_response(
			{'error': 'Internal Server Error'},
			status=500
		)


async def add_task(request):
	global task_counter, tasks
	try:
		data = await request.json()
		task_counter += 1
		task = {
			'id': task_counter,
			'title': data['title'],
			'completed': False
		}
		tasks[task_counter] = task
		return web.json_response({'status': f'task {task["id"]} added'}, status=201)
	except web.HTTPBadRequest as e:
		return web.json_response({'error': str(e)}, status=400)
	except Exception as e:
		print(f"Internal Server Error: {e}")
		return web.json_response({'error': 'Internal Server Error'}, status=500)


async def toggle_task(request):
	task_id = int(request.match_info['id'])
	if task_id not in tasks:
		raise web.HTTPNotFound()
	async with lock:
		task = tasks[task_id]
		task['completed'] = not task['completed']

	return web.json_response({'message': 'task updated'})


async def delete_task(request):
	task_id = int(request.match_info['id'])
	if task_id not in tasks:
		raise web.HTTPNotFound()

	async with lock:
		del tasks[task_id]

	return web.json_response({'message': 'task deleted'})


async def init_app():
	app = web.Application()
	app.router.add_get('/tasks', get_tasks)
	app.router.add_post('/add_task', add_task)
	app.router.add_put('/task/{id}', toggle_task)
	app.router.add_delete('/task/{id}', delete_task)

	return app


if __name__ == '__main__':
	web.run_app(init_app(), port=8081)
