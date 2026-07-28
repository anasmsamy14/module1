def process_squares(start, end):
    
    squares = [x**2 for x in range(start, end + 1)]
    
    
    evens = [s for s in squares if s % 2 == 0]
    odds = [s for s in squares if s % 2 != 0]
    
    print(f"Even squares: {evens}")
    print(f"Odd squares: {odds}")


process_squares(1, 5)
