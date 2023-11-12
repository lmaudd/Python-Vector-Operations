# Functions

def vec_add(): # Function to add two vectors together
   
    # Docstrings:
    """
    This function adds two vectors together and returns the resulting vector in component form.
    Separate vector components with a space (" ").
    """

    # Acquire vector number one
    v1 = input("What are the values in vector 1? (Space-Separated): ").split()
    for n in range(len(v1)):
        v1[n] = int(v1[n])

    # Acquire vector number two
    v2 = input("What are the values in vector 2? (Space-Separated): ").split()
    for n in range(len(v2)):
        v2[n] = int(v2[n])

    # Add vector one component to corresponding vector two component
    vsum=[]
    for i in range(len(v1)):
        n = v1[i]+v2[i]
        vsum.append(n)

    # Display the sum
    print(f"Your vector is {vsum}.")

def vec_sub(): # Function to subtract one vector from another
    
    # Docstrings:
    """
    This function subtracts one vector from another and returns the resulting vector in component form.
    Separate vector components with a space (" ").
    """

    # Acquire vector number one
    v1 = input("What are the values in vector 1? (Space-Separated): ").split()
    for n in range(len(v1)):
        v1[n] = int(v1[n])

    # Acquire vector number two
    v2 = input("What are the values in vector 2? (Space-Separated): ").split()
    for n in range(len(v2)):
        v2[n] = int(v2[n])

    # Subtract vector two component from corresponding vector one component
    vsum=[]
    for i in range(len(v1)):
        n = v1[i]-v2[i]
        vsum.append(n)

    # Display the difference
    print(f"Your vector is {vsum}.")

def vec_mult(): # Multiply one vector by a given scalar

    # Docstrings:
    """
    This function multiplies a vector by a scalar and returns the resulting vector in component form.
    Separate vector components with a space (" ").
    """

    # Acquire vector
    v1 = input("What are the values in vector 1? (Space-Separated): ").split()
    for n in range(len(v1)):
        v1[n] = int(v1[n])

    # Acquire scalar
    scalar = input("What is the magnitude of the scalar? ")
    scalar = int(scalar)

    # Multiply each vector component by scalar
    vproduct=[]
    for i in range(len(v1)):
        n = v1[i] * scalar
        vproduct.append(n)
    
    # Display resulting vector
    print(f"Your vector is {vproduct}.")

def vec_div(): # Divide a vector by a givens scalar
    
    # Docstrings:
    """
    This function divides a vector by a scalar and returns the resulting vector in component form.
    Separate vector components with a space (" ").
    """

    # Acquire vector
    v1 = input("What are the values in vector 1? (Space-Separated): ").split()
    for n in range(len(v1)):
        v1[n] = int(v1[n])

    # Acquire scalar
    scalar = input("What is the magnitude of the scalar? ")
    scalar = int(scalar)
    
    # Divide each vector component by scalar
    vquotient=[]
    for i in range(len(v1)):
        n = v1[i] / scalar
        vquotient.append(n)

    # Display quotient
    print(f"Your vector is {vquotient}.")

def vec_dp(): # Calculate dot product of two vectors

    # Docstrings:
    """
    This function calculates the dot product of two vectors and returns the resulting scalar in component form.
    Separate vector components with a space (" ").
    """

    # Acquire vector number one
    v1 = input("What are the values in vector 1? (Space-Separated): ").split()
    for n in range(len(v1)):
        v1[n] = int(v1[n])
    
    # Acquire vector number two
    v2 = input("What are the values in vector 2? (Space-Separated): ").split()
    for n in range(len(v2)):
        v2[n] = int(v2[n])

    # Compute dot product of the two vectors
    vcp=0
    for i in range(len(v1)):
        n = v1[i]*v2[i]
        vcp+=n

    # Display result
    print(f"Your scalar is {vcp}.")

def vec_cp(): # Calculate cross product

    # Docstrings:
    """
    This function calculates the cross product of two vectors and returns the resulting vector in standard form.
    Separate vector components with a space (" ").
    """

    print("Three-Dimensions Only...\n")

    # Acquiring vector one
    a = input("What are the values in vector 1? (Space-Separated): ").split()
    for n in range(len(a)):
        a[n] = int(a[n])

    # Acquire vector two
    b = input("What are the values in vector 2? (Space-Separated): ").split()
    for n in range(len(b)):
        b[n] = int(b[n])
    
    # Computing Cross Product
    i = a[1]*b[2] - a[2]*b[1]
    j = a[0]*b[2] - a[2]*b[0]
    k = a[0]*b[1] - a[1]*b[0]
    
    # Display result
    print(f"The cross product is: {i}i + {-j}j + {k}k")

def vec_projection(): # Project one vector onto another 
    
    # Docstrings:
    """
    This function calculates the the vector produced by projecting one vector (v1) onto another (v2).
    Separate vector components with a space (" ").
    """

    print("Two or Three Dimensions Only...\n")

    # Acquire vector number one
    v1 = input("What are the values in vector 1? (Space-Separated): ").split()
    for n in range(len(v1)):
        v1[n] = int(v1[n])

    # Acquire vector number two
    v2 = input("What are the values in vector 2? (Space-Separated): ").split()
    for n in range(len(v2)):
        v2[n] = int(v2[n])

    # Projection
    # Determine scalar by which to multiply vector
    a=0
    for i in range(len(v1)):
        n = v1[i] * v2[i]
        a+=n

    b=0
    for i in range(len(v1)):
        n = v2[i] * v2[i]
        b+=n
        
    c = a/b
    
    # Multiply vector by scalar
    vproj=[]
    for i in range(len(v2)):
        n = v2[i] * c
        vproj.append(n)

    # Display result
    print(f"The component of Vector 1 in the direction of Vector 2 is... {vproj}")