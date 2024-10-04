module F_using_nor(
    input w,
    input x,
    input y,
    input z,
    output F );
    wire w_n, x_n, y_n, z_n;
    wire wz_n, xz_n, wxy_n;
    assign w_n = ~(w | w);
    assign x_n = ~(x | x);
    assign y_n = ~(y | y);
    assign z_n = ~(z | z);
    assign wz_n = ~(w | z_n);
    assign xz_n = ~(x_n | z_n);
    assign wxy_n = ~(w_n | x_n | y_n);
    assign F = ~(wz_n | xz_n | wxy_n);
    // (x'+z')(w+z')(w'+x'+y')
endmodule

module F_using_nand(
    input w,
    input x,
    input y,
    input z,
    output F );
    wire w_n, x_n, y_n, z_n;
    wire wx_n, yz_n, wz_n;
    assign w_n = ~(w & w);
    assign x_n = ~(x & x);
    assign y_n = ~(y & y);
    assign z_n = ~(z & z);
    assign wx_n = ~(w & x_n);
    assign yz_n = ~(y_n & z_n);
    assign wz_n = ~(w_n & z_n);
    assign F = ~(wx_n & yz_n & wz_n);
    //  wx′ + y′z′ + w′z′
endmodule

module assignment1_230214();
    reg w, x, y, z;
    wire F_nor, F_nand;
    F_using_nor m((w), (x), (y), (z), (F_nor));
    F_using_nand n((w), (x), (y), (z), (F_nand));

    initial begin
        $dumpfile("assignment1_230214.vcd");
        $dumpvars(0, assignment1_230214);
    
        for (integer i = 0; i < 16; i++) begin
            {w, x, y, z} = i;
            #10;
        end
    end
endmodule
