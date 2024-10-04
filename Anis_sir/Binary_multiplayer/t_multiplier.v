module multiplier (output [5:0] P, input [2:0] A, B);
    assign P = A * B; // Multiplication of two 3-bit binary numbers
endmodule


module t_multiplier;
    reg [2:0] A, B;    // 3-bit input operands
    wire [5:0] P;      // 6-bit product output

    // Instantiate the multiplier
    multiplier m1 (P, A, B);

    // Initial block for test vectors and dumpfile
    initial begin
        // Create the dumpfile
        $dumpfile("t_multiplier.vcd"); // Generate dumpfile
        $dumpvars(0, t_multiplier);    // Dump all variables in the testbench module

        // Apply test cases
        A = 3'b000; B = 3'b000; #10;   // Test case 1: 0 * 0
        A = 3'b001; B = 3'b001; #10;   // Test case 2: 1 * 1
        A = 3'b010; B = 3'b001; #10;   // Test case 3: 2 * 1
        A = 3'b011; B = 3'b011; #10;   // Test case 4: 3 * 3
        A = 3'b100; B = 3'b010; #10;   // Test case 5: 4 * 2
        A = 3'b111; B = 3'b111; #10;   // Test case 6: 7 * 7

        // Add more test cases as needed
    end

    // End simulation after 100 time units
    initial #100 $finish;
endmodule
