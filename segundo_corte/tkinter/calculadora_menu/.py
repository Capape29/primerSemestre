def most():
        print(r[0])
        e=r[0]
        root = Tk()
        root.title("matriz A")
        root.config(bg="black")
        for g in range(len(e)):
            for c in range(len(e[g])):
                cell = Entry(root, width=10)
                cell.grid(row=g, column=c)
                cell.insert(0, '{}'.format(e[g][c]))
        root.mainloop()