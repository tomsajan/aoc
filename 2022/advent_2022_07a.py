from aocd import data, submit
# data = '''$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k'''


sizes = 0


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent


class Dir(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children_dir = {}
        self.children_file = {}

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.parent == other.parent and self.name == other.name

    def __hash__(self):
        return hash((type(self), self.name, self.parent))

    def __repr__(self):
        return f'Dir({self.name} (in {self.parent}))'

    def get_child_dir(self, name):
        return self.children_dir[name]

    def add_child(self, child):
        if isinstance(child, Dir):
            self.children_dir[child.name] = child

        if isinstance(child, File):
            self.children_file[child.name] = child

    def get_size(self):
        global sizes
        size = sum(int(c.size) for c in self.children_file.values())
        for d in self.children_dir.values():
            size += d.get_size()
        print(f'{self} {size}')
        if size <= 100000:
            sizes += size
        return size


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.size = None

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.parent == other.parent and self.name == other.name and self.size == other.size

    def __hash__(self):
        return hash((type(self), self.name, self.parent, self.size))

    def __repr__(self):
        return f'File({self.name} (in {self.parent}), {self.size})'

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

class Terminal:
    def __init__(self):
        self.root = Dir('/')
        self.cwd = self.root

    def process_command(self, command):
        if command.startswith('cd '):
            dir_name = command.replace('cd ', '').strip()
            if dir_name == '..':
                self.cwd = self.cwd.get_parent()
                print(f'goint to .. {self.cwd}')
            else:
                self.cwd = self.cwd.get_child_dir(dir_name)
                print(f'goint to {self.cwd}')
            if self.cwd is None:
                raise Exception('cwd is None')

        elif command.startswith('ls'):
            print('ls command')
            # no action required
            pass
        else:
            raise Exception(f'unknown command {command}')

    def process_output(self, output):
        if output.startswith('dir '):
            d = Dir(output.replace('dir ', '').strip())
            d.set_parent(self.cwd)
            self.cwd.add_child(d)
            print(f'new dir {d}')
        else:
            size, name = output.strip().split()
            f = File(name)
            f.set_size(size)
            f.set_parent(self.cwd)
            self.cwd.add_child(f)
            print(f'new file {f}')


    def process_line(self, line):
        if line.startswith('$ '):
            self.process_command(line.replace('$ ', ''))
        else:
            self.process_output(line)


if __name__ == '__main__':

    t = Terminal()
    for line in data.split('\n')[1:]:
        t.process_line(line)
    print(t)
    t.root.get_size()
    print(sizes)
    submit(sizes)
