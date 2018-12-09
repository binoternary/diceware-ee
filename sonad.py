#! /usr/bin/env python3
# coding=utf-8

import random as rnd
import sys

def main():
    rnd.seed(0)
    file = sys.argv[1]
    with open(file, 'r') as f:
        lines = f.readlines()

    dice_per_word = 5
    dice_faces = 6
    n_words = dice_faces ** dice_per_word
    assert len(lines) >= n_words

    selected_words = sorted(rnd.sample(lines, n_words))
    indexed_words = zip(word_indexes(dice_per_word, dice_faces), selected_words)

    for i, iw in enumerate(indexed_words):
        print("{}\t{}".format(iw[0], iw[1].strip()))


def word_indexes(dice_per_word=5, dice_faces=6):
    max_val = dice_faces
    max_idx = [max_val for i in range(dice_per_word)]
    idx = [1 for i in range(dice_per_word)]
    while idx <= max_idx:
        yield "".join(map(str, idx))
        idx[-1] += 1
        for i in range(1, dice_per_word):
            if idx[-i] > max_val:
                if i == 0:
                    break
                else:
                    idx[-i] = 1
                    idx[-(i + 1)] += 1
            else:
                break

if __name__ == '__main__':
    main()
