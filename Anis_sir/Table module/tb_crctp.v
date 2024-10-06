primitive crctp (X, A, B, C);
    output X;          
    input A, B, C;   

    // Truth table for X(A,B,C)
    table
        // A B C : X (Output)
        0 0 0 : 1;     // minterm 0
        0 0 1 : 0;     // minterm 1
        0 1 0 : 1;     // minterm 2
        0 1 1 : 0;     // minterm 3
        1 0 0 : 1;     // minterm 4
        1 0 1 : 0;     // minterm 5
        1 1 0 : 1;     // minterm 6
        1 1 1 : 1;     // minterm 7
    endtable
endprimitive
module tb_crctp;
    // Inputs
    reg A, B, C;
    
    // Output
    wire X;

    // Instantiate the primitive (crctp)
    crctp x (X, A, B, C);

    // Testbench logic
    initial begin
        // Dump waveform for analysis
        $dumpfile("tb_crctp.vcd");
        $dumpvars(0, tb_crctp);
        
        // Test cases
        A = 0; B = 0; C = 0; #10;  // Expected output X = 1
        A = 0; B = 0; C = 1; #10;  // Expected output X = 0
        A = 0; B = 1; C = 0; #10;  // Expected output X = 1
        A = 0; B = 1; C = 1; #10;  // Expected output X = 0
        A = 1; B = 0; C = 0; #10;  // Expected output X = 1
        A = 1; B = 0; C = 1; #10;  // Expected output X = 0
        A = 1; B = 1; C = 0; #10;  // Expected output X = 1
        A = 1; B = 1; C = 1; #10;  // Expected output X = 1

        $finish;  // End simulation
    end
endmodule
