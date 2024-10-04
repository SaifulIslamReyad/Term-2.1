module half_adder (output S, C, input x, y);
	xor (S, x, y);
	and (C, x, y);
endmodule

module full_adder (output S, C, input x, y, z); 
	wire S1, C1, C2;
	half_adder HA1 (S1, C1, x, y);
	half_adder HA2 (S, C2, S1, z);
	or G1 (C, C2, C1);
endmodule

module adder_substractor (output [2:0] S, output C3, input [2:0] A, B, input M);
    wire B01, B02, B03;
    xor(B01, B[0], M);
    xor(B02, B[1], M);
    xor(B03, B[2], M);
    wire C1, C2;
    full_adder
        FA0 (S[0], C1, A[0], B01, M),
		FA1 (S[1], C2, A[1], B02, C1),
		FA2 (S[2], C3, A[2], B03, C2);
endmodule

module t_adder_substractor;
	wire c3;
	wire [2:0] S;
	reg [2:0] A, B;
	reg M;
	adder_substractor add_sub (S, C3, A, B, M);

	initial begin
		$dumpfile("t_adder_substractor.vcd"); 
		$dumpvars(0, t_adder_substractor);    

		A = 3'b101; B = 3'b011; M = 1'b0;
		#10 A = 3'b101; B = 3'b011; M = 1'b1;
		#10 A = 3'b011; B = 3'b101; M = 1'b1;
		#10 A = 3'b111; B = 3'b000; M = 1'b0;
		#10 A = 3'b111; B = 3'b000; M = 1'b1;
		#10 A = 3'b000; B = 3'b111; M = 1'b1;
		#10 A = 3'b101; B = 3'b101; M = 1'b0;
		#10 A = 3'b101; B = 3'b101; M = 1'b1;
	end

	initial #250 $finish;
	
endmodule
