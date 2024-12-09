import sys
import tqdm

def parse(data):
    index = []
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            index.append((int(data[i]), int(data[i+1])))
        else:
            index.append((int(data[i]), 0))

    disk = []
    for i, t in enumerate(index):
        for _ in range(t[0]):
            disk.append(i)
        for _ in range(t[1]):
            disk.append(None)
    return disk

def last_block(disk):
    last = None
    bo = False
    for i, block in enumerate(disk):
        if block is None:
            bo = True
        if block is not None and bo:
            last = (i, block)
    return last

def compact_disk(disk):
    compacted_disk = disk.copy()
    br = disk.count(None)
    for i, block in tqdm.tqdm(enumerate(compacted_disk), total=len(compacted_disk)):
        if block is None:
            tmp = last_block(compacted_disk)
            if tmp is not None:
                compacted_disk[tmp[0]] = None
                compacted_disk[i] = tmp[1]
        # if i >= len(compacted_disk) - br:
        #     break

    return compacted_disk

def calculate_checksum(disk):
    return sum(position * block for position, block in enumerate(disk) if block is not None)

def solve(data):
    disk = parse(data)
    while True:
        compacted_disk = compact_disk(disk)
        if compacted_disk == disk:
            break
        disk = compacted_disk
    return calculate_checksum(disk)

def main():
    data = sys.stdin.read().strip()
    print(solve(data))

if __name__ == '__main__':
    main()
