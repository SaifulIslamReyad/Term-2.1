module my_circuit_prop_delay (A, B, C, D, E);
    output D, E;
    input A, B, C;
    wire W1, W2, W3;
    and (W1, A, B);
    not (W2, W1);
    or  (D, W2, C);
    assign E = W1;
endmodule


module t_my_circuit_prop_delay;
    wire D, E;
    reg A, B, C;

    my_circuit_prop_delay x (A, B, C, D, E);

    initial begin
        $dumpfile("t_my_circuit_prop_delay.vcd");
        $dumpvars(0, t_my_circuit_prop_delay);

        // Monitor changes in A, B, C, D, and E
        $monitor("Time: %0t | A = %b, B = %b, C = %b, D = %b, E = %b", $time, A, B, C, D, E);

        // Apply different input values and display results
        A = 0; B = 0; C = 0; #10;
        $display("Time: %0t - Applied A=0, B=0, C=0", $time);

        A = 0; B = 0; C = 1; #10;
        $display("Time: %0t - Applied A=0, B=0, C=1", $time);

        A = 0; B = 1; C = 0; #10;
        $display("Time: %0t - Applied A=0, B=1, C=0", $time);

        A = 0; B = 1; C = 1; #10;
        $display("Time: %0t - Applied A=0, B=1, C=1", $time);

        A = 1; B = 0; C = 0; #10;
        $display("Time: %0t - Applied A=1, B=0, C=0", $time);

        A = 1; B = 0; C = 1; #10;
        $display("Time: %0t - Applied A=1, B=0, C=1", $time);

        A = 1; B = 1; C = 0; #10;
        $display("Time: %0t - Applied A=1, B=1, C=0", $time);

        A = 1; B = 1; C = 1; #10;
        $display("Time: %0t - Applied A=1, B=1, C=1", $time);

        $finish;
    end
endmodule

