from __init__ import Job, Task, RemoteCmd

def main():
	job = Job([
		("title", "a render test"),
		("subtasks", []),
	])
	task = Task([
		("title", "render a.rib"),
		("cmds", [
			RemoteCmd([
				("", "prman -Progress /net/my_ribs/a.rib"),
				("service", "PixarRender"),
			]),
			RemoteCmd([
				("", "prman -Progress /net/my_ribs/a.rib"),
				("service", "PixarRender"),
			]),
			RemoteCmd([
				("", "prman -Progress /net/my_ribs/a.rib"),
				("service", "PixarRender"),
			]),
		]),
	])
	job.set("subtasks", task)
	print(job.toString())

main()
