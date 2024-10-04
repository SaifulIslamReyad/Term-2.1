module decrement(input [2:0] A, output [2:0] Y);
    wire C1, C2;
    FullAdder fa0 (A[0], 1'b1, 1'b0, Y[0], C1);
    FullAdder fa1 (A[1], 1'b1, C1, Y[1], C2);
    FullAdder fa2 (A[2], 1'b1, C2, Y[2], );
endmodule

module FullAdder(input A, input B, input Cin, output Sum, output Cout);
    assign Sum = A ^ B ^ Cin;
    assign Cout = (A & B) | (A & Cin) | (B & Cin);
endmodule

module _230214;
    reg [2:0] A;
    wire [2:0] Y;
    decrement uut (A, Y);
    initial begin
        $dumpfile("_230214.vcd");
        $dumpvars(0, _230214);
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