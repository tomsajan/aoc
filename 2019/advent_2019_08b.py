from aocd import data, submit


def chunks(L, n):
    """ Yield successive n-sized chunks from L.
    """
    for i in range(0, len(L), n):
        yield L[i:i+n]


def split_str(data):
    return [char for char in data]


def get_num_count(data, num):
    return len(list(filter(lambda x: x == num, data)))


if __name__ == '__main__':
    dimx = 25
    dimy = 6

    # data = '0222112222120000'
    # dimx = 2
    # dimy = 2

    layer_pixels = dimx * dimy
    layers = [split_str(chunk) for chunk in chunks(data, layer_pixels)]
    stacked_layers = list(zip(*layers))
    layer_selection = []
    for stack in stacked_layers:
        # broken = False
        for pixel in stack:
            if pixel != '2':
                layer_selection.append(pixel)
                # broken = True
                break
        # if not broken:
        #     layer_selection.append('2')

    print(''.join(layer_selection))
    # submit(''.join(layer_selection))

    image_rows = chunks(layer_selection, dimx)
    for row in image_rows:
        print(''.join(row).replace('0', ' '))

    submit('EJRGP')