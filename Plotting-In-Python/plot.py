import matplotlib.pyplot as plt


def print_line_graph(plt):
    plt.plot ([1,2,3,4], [1,4,8,16])
    plt.ylabel('y numbers')
    plt.xlabel('x numbers')
    plt.show()

def print_bar_graph(plt):
    fig, ax = plt.subplots()
    fruits = ["apple", 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')
    plt.show()

if __name__ == "__main__":
    print_line_graph(plt)
    print_bar_graph(plt)



