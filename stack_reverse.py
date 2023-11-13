def reverse(sentence):
    stack = []
    for character in sentence:
        stack+=character

    reverse_sentence= ""
    x=-1
    for i in range(len(stack)):
        reverse_sentence += stack[x]
        x-=1
        

    return reverse_sentence


input_sentence = input("Bir cümle girin: ")
reverse_sentence = reverse(input_sentence)
print("Tersine çevrilmiş cümle:", reverse_sentence)
