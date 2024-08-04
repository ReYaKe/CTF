from pwn import *
#pwntools is sick for CTF type of connections just fyi! (Mightve been good for the Lights out challenge last week >:I)

def receive_data(conn, delimiter=b'\n'):
    data = conn.recvuntil(delimiter)
    print(f"Received {len(data)} bytes")
    return data.decode().rstrip(delimiter.decode())

def receive_small_data(conn, buffer_size=1024):
    data = conn.recv(buffer_size)
    print(f"Received {len(data)} bytes")
    return data.decode()

def main():
    host = 'challs.n00bzunit3d.xyz' #replace with host and port obv
    port = 10071
    loop = 0
    conn = remote(host, port)

    data = receive_data(conn, delimiter=b'\n')
    print(data)
    a = list(map(int, data.split()))
    print("Received numbers:", len(a))

    for _ in range(20):
        c = max(a) // 2  #Using max of the array was the most consistent as using median/mean or anything other always ended with lots of outliers(likely due to the sheer size of 696969 numbers
      
        a = [abs(c - x) for x in a]
      
        conn.sendline(str(c).encode())
      
        print("Sending input:", c)
        print("Current Loop: ", loop)
        print("Maximum of the Array: ", max(a))
        print("Minimum of the Array: ", min(a))
        print("Len of the Set: ", len(set(a)))
        print("Len of the Array: ", len(a))
        loop += 1
  
        if len(set(a)) == 1:   # We know this is what the server is looking for so no need to listen for response every time
            response = receive_small_data(conn)
            if "n00bz" in response:
                print("Flag received:", response) 
                break

    conn.close()

if __name__ == "__main__":
    main()
