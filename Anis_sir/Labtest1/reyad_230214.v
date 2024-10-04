module decrement(input [2:0] A, output [2:0] Y);
    wire b0, b1, A0_not, A1_not, A2_not;
    assign A0_not = ~A[0];
    assign A1_not = ~A[1];
    assign A2_not = ~A[2];
    assign Y[0] = A0_not;
    assign b0 = A[0] & A[0];
    assign Y[1] = A1_not ^ b0;
    assign b1 = (A[1] & b0) | (A[1] & A0_not);
    assign Y[2] = A2_not ^ b1;
endmodule

module reyad_230214;
    reg [2:0] A;
    wire [2:0] Y;
    decrement uut (A, Y);
    initial begin
        $dumpfile("reyad_230214.vcd");
        $dumpvars(0 ,reyad_230214);
        $monitor("Time = %0t, A = %b, Y = %b", $time, A, Y);
        A = 3'b000; #10;
        A = 3'b001; #10;
        A = 3'b010; #10;
        A = 3'b011; #10;
        A = 3'b100; #10;
        A = 3'b101; #10;
        A = 3'b110; #10;
        A = 3'b111; #10;
        $finish;
    end
endmodule