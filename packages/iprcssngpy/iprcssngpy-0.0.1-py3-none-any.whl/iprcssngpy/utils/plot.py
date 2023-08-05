import matplotlib.pyplot as plt


def plot_image(img):
    plt.figure(figsize=(12, 4))
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()


def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))
    names_lst = ['image {}'.format(i) for i in range(1, number_images + 1)]
    names_lst.append('Result')

    for ax, name, img in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(img, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()


def plot_histogram(img):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color.title()))
        ax.hist(img[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
    fig.tight_layout()
    plt.show()
