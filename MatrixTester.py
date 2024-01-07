import MatrixLover

def main():

    #creating matrices
    trixie = MatrixLover.Matrix(3,4)                                
    alice = MatrixLover.Matrix(3,4)
    chloe = MatrixLover.Matrix(4,3)
    christian = MatrixLover.Matrix(3,3)
    
    #randomizing matrices
    MatrixLover.Matrix.randomize(trixie,0,9)
    MatrixLover.Matrix.randomize(alice,0,9)
    MatrixLover.Matrix.randomize(chloe,0,9)
    MatrixLover.Matrix.randomize(christian,0,9)

    #printing matrices
    print("trixie:")
    trixie.print()
    print("alice:")
    alice.print()
    print("chloe:")
    chloe.print()

    #plus function test
    added = trixie.plus(alice)
    print("sum of trixie and alice:")
    added.print()

    #times function test
    multiplied = trixie.times(chloe)
    print("product of trixie and chloe:")
    multiplied.print()
    
    #scalarTimesRow function test
    print("chloe with row 1 multiplied by 5:")
    MatrixLover.Matrix.scalarTimesRow(chloe,0,5)
    chloe.print()

    #switchRows function test
    print("chloe with row 1 switched with row 2:")
    MatrixLover.Matrix.switchRows(chloe,0,1)
    chloe.print()

    #linearCombRows function test
    print("chloe with row 1 multiplied by 5 added to row 2:")
    MatrixLover.Matrix.linearCombRows(chloe,5,0,1)
    chloe.print()

    #rowreduce function test
    print("alice:")
    alice.print()
    print("alice RREF:")
    MatrixLover.Matrix.rowreduce(alice)
    alice.print()

    #invert function test
    print("christian:")
    christian.print()
    print("christian inverted:")
    inverted = MatrixLover.Matrix.invert(christian)
    inverted.print()



if __name__ == "__main__":
    main()