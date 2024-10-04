// Module Definition
module my_circuit_prop_delay (A, B, C, D, E);
    output D, E;
    input A, B, C;
    
    wire W1, W2, W3;
    and (W1, A, B);
    not (W2, W1);
    or  (D, W2, C);
    assign E = W1;   // Assuming E = A AND B (as an example)
endmodule

// Testbench Definition
module t_my_circuit_prop_delay;
    wire D, E;
    reg A, B, C;
    
    // Instantiate the design under test (DUT)
    my_circuit_prop_delay x (A, B, C, D, E);

    // Initial Block for Test Cases
    initial begin
        // Create a VCD file for waveform analysis
        $dumpfile("t_my_circuit_prop_delay.vcd"); // Create the VCD file
        $dumpvars(0, t_my_circuit_prop_delay); // Dump all variables in the testbench

        // Test all combinations of A, B, C with concise format
        A = 0; B = 0; C = 0; #10;
        A = 0; B = 0; C = 1; #10;
        A = 0; B = 1; C = 0; #10;
        A = 0; B = 1; C = 1; #10;
        A = 1; B = 0; C = 0; #10;
        A = 1; B = 0; C = 1; #10;
        A = 1; B = 1; C = 0; #10;
        A = 1; B = 1; C = 1; #10;

        $finish; // End simulation
    end
endmodule
