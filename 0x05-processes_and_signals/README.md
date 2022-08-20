# LINUX PROCESS & SIGNALS

In this project, I learned about Linux processes. A **process** is an instance of a program. Each process has its own unique process ID every time it is created. This **PID** is always a non-negative integer value.

I also learnt various commands that I can use to do various things such as:
	1. **pgrep** - looks through the currently running processes and lists the process IDs which match the selection criteria to stdout.
	2. **ps** - reports a snapshot of the current processes.
	3. **top** - display Linux processes.
	4. **kill** - sends a signal to a process.

A **signal** refers to a sofware interrupt. They are a way to deliver asynchronous events to the application. In Linux, every signal has a name that begins with the characters SIG.

Information on current processes is stored in the */proc* filesystem. This filesystem consists of kernel data that changes in real time (i.e., sensing and responding to external events nearly simultaneously). It is easy to extract the information contained therein using commands such as cat. 
