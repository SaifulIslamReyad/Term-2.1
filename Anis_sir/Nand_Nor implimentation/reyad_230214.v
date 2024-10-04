module NOR_gate(
	input w, x, y, z,
	output  f_NOR);
	wire w1, w2, w3, w4, A, B, C;
	nor G1(w1, w, w);
	nor G2(w2, x, x);
	nor G3(w3, y, y);
	nor G4(w4, z, z);
	nor G5(A, w, w4);
	nor G6(B, w2, w4);
	nor G7(C, w1, w2, w3);
	nor G8(f_NOR, A, B, C);
endmodule


module NAND_gate(
	input w, x, y, z,
	output  f_NAND);
	wire w1, w2, w3, w4, A, B, C;
	nand G1(w1, w, w);
	nand G2(w2, x, x);
	nand G3(w3, y, y);
	nand G4(w4, z, z);
	nand G5(A, w, w2);
	nand G6(B, w3, w4);
	nand G7(C, w1, w4);
	nand G8(f_NAND, A, B, C);
endmodule


module reyad_230214;
	wire F_NOR, F_NAND;
	reg w, x, y, z;
	NOR_gate N(w, x, y, z, F_NOR);
	NAND_gate A(w, x, y, z, F_NAND);
	initial begin
		$dumpfile("reyad_230214.vcd");
		$dumpvars(0, reyad_230214);
		w = 1'b0;x = 1'b0;y = 1'b0;z = 1'b0;
		#10 w = 1'b0;x = 1'b0;y = 1'b0;z = 1'b1;
		#10 w = 1'b0;x = 1'b0;y = 1'b1;z = 1'b0;
		#10 w = 1'b0;x = 1'b0;y = 1'b1;z = 1'b1;
		#10 w = 1'b0;x = 1'b1;y = 1'b0;z = 1'b0;
		#10 w = 1'b0;x = 1'b1;y = 1'b0;z = 1'b1;
		#10 w = 1'b0;x = 1'b1;y = 1'b1;z = 1'b0;
		#10 w = 1'b0;x = 1'b1;y = 1'b1;z = 1'b1;
		#10 w = 1'b1;x = 1'b0;y = 1'b0;z = 1'b0;
		#10 w = 1'b1;x = 1'b0;y = 1'b0;z = 1'b1;
		#10 w = 1'b1;x = 1'b0;y = 1'b1;z = 1'b0;
		#10 w = 1'b1;x = 1'b0;y = 1'b1;z = 1'b1;
		#10 w = 1'b1;x = 1'b1;y = 1'b0;z = 1'b0;
		#10 w = 1'b1;x = 1'b1;y = 1'b0;z = 1'b1;
		#10 w = 1'b1;x = 1'b1;y = 1'b1;z = 1'b1;
		#10 w = 1'b1;x = 1'b1;y = 1'b1;z = 1'b0;
	end
	initial #200 $finish;
endmodule
	

	