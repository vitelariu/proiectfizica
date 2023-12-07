from manim import *



def intro_0(self : Scene):
    text = Tex("Motorul diesel").scale(2)
    text2 = Paragraph("-Vitelariu Paul", "-Iustinian Petrisor", "-Calugaru Teodor", "-Muraru Vlad").shift(1.5 * DOWN).scale(0.5)
    self.play(Write(text, run_time=1.5))
    self.play(Write(text2))
    self.wait(0.5)
    self.remove(text, text2)

    quote = Paragraph("\"Nimic nu este sigur in viata, cu exceptia mortii, a taxelor", "si a doua lege a termodinamicii\"", "-Seth Lloyd", t2c={"sigur":YELLOW, "a doua lege a termodinamicii":BLUE}, t2s={'Seth Lloyd':ITALIC})
    quote.scale(0.6)
    quote.to_edge(UP)

    self.play(Write(quote), run_time = 3)
    self.wait(3)
    self.remove(quote)


def intro(self : Scene):
    #intro1
    m = 1.1
    n = 0.5



    dashline = DashedLine(n*LEFT+m*UP, m*UP, dash_length=n)
    injector = Line(UP*0.2, DOWN*0.2).next_to(dashline, RIGHT, buff=0).shift(UP*0.1)
    dashline2 = DashedLine(m*UP, n*RIGHT+m*UP, dash_length=n)

    line_t = Line(n*LEFT+m*UP, m*UP)
    line_t2 = Line(m*UP, n*RIGHT+m*UP)

    line1 = Line(n*LEFT + m * UP, n*LEFT + m * DOWN)
    line3 = Line(n*RIGHT+m*DOWN, n*RIGHT+m*UP)
    plot = VGroup(line1, line3, line_t, line_t2, injector)
    circle = Line(n*LEFT + m * DOWN, n*RIGHT+m*DOWN)
    circle.set_path_arc(5)
    point = Dot(radius = 0.1, color=WHITE).move_to(circle.get_center())
    
    plot.add(circle, point)

    sp = Rectangle(color=YELLOW, height=5, width=10).move_to(plot.get_center())

    text = Tex("In capitolul 1: Functionarea motorului diesel").next_to(sp, UP, buff=0.1)






    circ = Circle(radius=0.6, stroke_opacity=0).move_to(point.get_center())
    dotpos = ValueTracker(PI/2)
    dot1 = always_redraw(lambda:
        Dot().move_to(circ.point_at_angle(dotpos.get_value()))
    )

    lineLength = 1.5
    dot2 = Dot(fill_opacity=1)
    dot2 = always_redraw(lambda:
        dot2.move_to(
            [0, dot1.get_center()[1]+np.sqrt(lineLength**2 - dot1.get_center()[0]**2), 0]
        )
    )


    piston= Rectangle(height=0.4, width = 2*n).next_to(dot2, UP, buff=0)

    line = always_redraw(lambda:
        Line(dot1.get_center(), dot2.get_center())
    )
    plot.add(dot1, dot2, circ, line, piston)
    piston = always_redraw(lambda : piston.next_to(dot2, UP, buff=0))
 
    self.play(FadeIn(plot))
    plot.add(sp)
    self.play(Create(sp), Write(text))

    def update_line_t(x):
        if (dotpos.get_value() / PI) % 4 > 1/2 and (dotpos.get_value() / PI) % 4 <= 3/2:
            x.set_opacity(0)
        else:
            x.set_opacity(1)
    def update_dashed_for_line_t(z):
        if (dotpos.get_value() / PI) % 4 > 1/2 and (dotpos.get_value() / PI) % 4 <= 3/2:
            z.set_opacity(1)
        else:
            z.set_opacity(0)

    def update_line_t2(x):
        if (dotpos.get_value() / PI - 0.5) % 4 > 3 and (dotpos.get_value() / PI - 0.5) % 4<= 4:
            x.set_opacity(0)
        else:
            x.set_opacity(1)
    def update_dashed_for_line_t2(z):
        if (dotpos.get_value() / PI - 0.5) % 4 > 3 and (dotpos.get_value() / PI - 0.5) % 4 <= 4:
            z.set_opacity(1)
        else:
            z.set_opacity(0)
    def update_injector(x):
        if (dotpos.get_value() /PI) % 4 > 5/2 and (dotpos.get_value() /PI) % 4 < 2.8:
            x.set_color(RED)
        else:
            x.set_color(WHITE)


    line_t.add_updater(update_line_t)
    self.add(dashline)
    dashline.add_updater(update_dashed_for_line_t)
    line_t2.add_updater(update_line_t2)
    self.add(dashline2)
    dashline2.add_updater(update_dashed_for_line_t2)
    injector.add_updater(update_injector)

    self.play(dotpos.animate.set_value((PI/2 + 2*PI)*5), rate_func=rate_functions.smoothstep, run_time=4)
    self.wait(2)


    self.play(
        FadeOut(text),
        plot.animate.scale(0.1).to_corner(UL)
    )


    #intro2
    number_plane = NumberPlane(
            x_range=(-1, 20, 1),
            y_range=(-1, 10, 1),
            x_length=8,
            y_length=4,
            background_line_style={"stroke_opacity": 0.6},
            axis_config={"include_tip": True}
    ).shift(0.9*DOWN)
    x_label = number_plane.get_x_axis_label("V")
    y_label = number_plane.get_y_axis_label("P")
    plot2 = VGroup(number_plane, x_label, y_label) 

    self.play(FadeIn(plot2))
    sp2 = Rectangle(color=YELLOW, height=5, width=10).move_to(plot2.get_center())
    text2 = Tex("In capitolul 2: Ciclul motorului diesel").next_to(sp2, UP, buff=0.1)
    self.play(Create(sp2), Write(text2))
    plot2.add(sp2)
    self.wait(1)

    p0 = Dot(2.5*LEFT+2*DOWN)
    point1 = Dot(2.5*RIGHT+2*DOWN)
    point2 = Dot(2.5*LEFT +0.5*UP)
    point3 = Dot(0.5*UP + 0.7*LEFT)
    point4 = Dot(2.5*RIGHT + 0.8*DOWN)
    line0_1 = Line(2.5*LEFT+2*DOWN, 2.5*RIGHT+2*DOWN)
    line1_2 = Line(2.5*RIGHT+2*DOWN, 2.5*LEFT +0.5*UP)
    line2_3 = Line(2.5*LEFT +0.5*UP, 0.5*UP + 0.7*LEFT)
    line3_4 = Line(0.5*UP + 0.7*LEFT, 2.5*RIGHT + 0.8*DOWN)
    line4_1 = Line(2.5*RIGHT + 0.8*DOWN, 2.5*RIGHT+2*DOWN)

    line1_2.set_path_arc(-1)
    line3_4.set_path_arc(0.7)

    number0 = Tex("0").next_to(p0, LEFT)
    number1 = Tex("1").next_to(point1, RIGHT)
    number2 = Tex("2").next_to(point2, LEFT)
    number3 = Tex("3").next_to(point3, RIGHT)
    number4 = Tex("4").next_to(point4, RIGHT)

    self.play(
        Create(p0), Create(point1), Create(line0_1), Create(number0), Create(number1), run_time=0.5
    )
    self.play(
        Create(point2), Create(line1_2), Create(number2), run_time=0.5
    )
    self.play(
        Create(point3), Create(line2_3), Create(number3), run_time=0.5
    ) 
    self.play(
        Create(point4), Create(line3_4), Create(number4), run_time=0.5
    )
    self.play(
        Create(line4_1), run_time=0.5
    )
    plot2.add(p0, point1, point2, point3, point4, line0_1, line1_2, line2_3, line3_4, line4_1, number0, number1, number2, number3, number4)
    self.play(
        FadeOut(text2),
        plot2.animate.scale(0.1).to_corner(UL).shift(RIGHT * 4)
    )


    #intro3
    ef_text = Tex("Formula eficientei este:").shift(UP*1.5)
    ef_formula = MathTex("\\eta = 1 - \\gamma \\frac{T_4 - T_1}{T_3- T_2}").move_to(ef_text.get_center()).shift(1.5*DOWN+0.15*RIGHT)
    plot3 = Group(ef_text, ef_formula)
    plot3.scale(0.8)

    sp3 = Rectangle(color=YELLOW, height=5, width=10).move_to(plot3.get_bottom()).shift(DOWN * 0.3)
    plot3.add(sp3)
    text3 = Tex("In capitolul 3: Eficienta motorului Diesel").next_to(sp3, UP, buff=0.1)

    pic = SVGMobject("assets/PiCreature/PiCreatures_erm.svg", height=1.2).move_to(ef_formula.get_center()).shift(2.5*DOWN+3.6*LEFT)
    pic2 = SVGMobject("assets/PiCreature/PiCreatures_angry.svg", height=1.2).move_to(ef_formula.get_center()).shift(2.5*DOWN+3.6*LEFT)
    speech = ImageMobject("assets/PiCreature/Bubbles_speech_white.png").scale(0.2).move_to(pic.get_top()).shift(0.75*UP + 1.2*RIGHT)
    speech_text = Tex("N-are sens!").scale(0.6).move_to(speech.get_center()).shift(0.25*UP)
    self.play(Create(sp3), Create(text3))
    self.play(FadeIn(ef_text), Write(ef_formula), FadeIn(pic))
    self.wait(2)
    self.play(Transform(pic, pic2), FadeIn(speech), Write(speech_text))
    self.wait(5)

    plot3.add(pic, pic2, speech, speech_text)

    self.play(
        FadeOut(text3), 
        plot3.animate.scale(0.1).to_corner(UR).shift(LEFT * 4)
    )



    #intro4
    rudolf = ImageMobject("assets/Rudolf_Diesel.jpg").scale(0.8).shift(DOWN * 0.75)
    self.play(FadeIn(rudolf))
    
    sp4 = Rectangle(color=YELLOW, height=5, width=10).move_to(rudolf.get_center())
    text4 = Tex("In capitolul 4: Istoria Motorului Diesel").next_to(sp4, UP, buff=0.1)
    self.play(Create(sp4), Create(text4))
    self.wait(2)

    rudolf.add_updater(lambda x: x.move_to(sp4.get_center()))
    self.play(
        FadeOut(text4),
        sp4.animate.scale(0.1).to_corner(UR),
        rudolf.animate.scale(0.1)
    )

    self.wait(1)
    self.remove(plot, plot2, plot3, rudolf, sp4, sp2, line0_1, line1_2, line2_3, line3_4, line4_1, number0, p0, number1, number2, number3, number4, point1, point2, point3, point4)





def observa_ce_nu_spun(self : Scene):
    text = Tex("Un timp = Un proces termodinamic").shift(UP * 3)
    strikethrough = Line(LEFT*4.5, RIGHT*4.5, color=RED).move_to(text.get_center())


    pi1 = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").scale(1).to_corner(DL)
    pi2 = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").scale(1).next_to(pi1, RIGHT)
    pi3 = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").scale(1).next_to(pi2, RIGHT)

    pi2_ask = SVGMobject("assets/PiCreature/PiCreatures_raise_left_hand.svg").move_to(pi2.get_center())
    pi2_question = ImageMobject("assets/PiCreature/Bubbles_speech_white.png").scale(0.3).next_to(pi2, UP).shift(RIGHT*2)
    pi2_question_text = Tex("Ce vrea asta sa insemne?").scale(0.5).move_to(pi2_question.get_center()).shift(UP*0.35)


    teacher_plain = SVGMobject("assets/PiCreature/plain_teacher.svg").scale(1.3).to_corner(DR)
    teacher_well = SVGMobject("assets/PiCreature/well_teacher.svg").scale(1.3).move_to(teacher_plain.get_center())
    
    pi_teacher_question = ImageMobject("assets/PiCreature/Bubbles_speech_white_flip.png").scale(0.3).next_to(teacher_plain, UP).shift(LEFT*2)
    pi_teacher_question_text = Tex("Veti vedea in Cap. 2").scale(0.6).move_to(pi_teacher_question.get_center()).shift(UP*0.35)



    plot = Group(pi1, pi2, pi3, teacher_plain, text)
    
    self.add((plot))
    self.wait(4)
    self.play(Create(strikethrough))
    self.wait(1)
    self.play(ReplacementTransform(pi2, pi2_ask), FadeIn(pi2_question), Write(pi2_question_text))
    self.wait(1)
    self.play(ReplacementTransform(teacher_plain, teacher_well))
    self.play(FadeIn(pi_teacher_question))
    self.play(Write(pi_teacher_question_text))
    self.wait()
    self.play(FadeOut(pi2_question), FadeOut(pi2_question_text))

    pi1_transform = SVGMobject("assets/PiCreature/PiCreatures_shruggie.svg").move_to(pi1.get_center())
    pi2_transform = SVGMobject("assets/PiCreature/PiCreatures_confused.svg").move_to(pi2_ask.get_center())
    pi3_transform = SVGMobject("assets/PiCreature/PiCreatures_maybe.svg").move_to(pi3.get_center())
    self.play(ReplacementTransform(pi2_ask, pi2_transform), ReplacementTransform(pi1, pi1_transform), ReplacementTransform(pi3, pi3_transform))

    self.wait(3)
    self.remove(plot, strikethrough, pi1_transform, pi2_transform, pi3_transform, pi2_ask, pi2_question, pi2_question_text, teacher_plain, teacher_well, pi_teacher_question, pi_teacher_question_text)



def observa_ce_nu_spun2(self : Scene):
    text = Tex("Un timp = Un proces termodinamic").shift(UP * 3)
    strikethrough = Line(LEFT*4.5, RIGHT*4.5, color=RED).move_to(text.get_center())

    teacher_well = SVGMobject("assets/PiCreature/well_teacher.svg").scale(1.3).to_corner(DR)

    pi1 = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").to_corner(DL)
    pi2 = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").next_to(pi1, RIGHT)
    pi3 = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").next_to(pi2, RIGHT)


    plot = Group(teacher_well ,text, strikethrough, pi1, pi2, pi3)
    self.add((plot))
    self.wait()
    timp1 = MathTex("\\text{Timpul 1: } 0 \\rightarrow 1 \\text{(un proces)}").next_to(text, DOWN).shift(DOWN*0.3)
    timp2 = MathTex("\\text{Timpul 2: } 1 \\rightarrow 2 \\text{(un proces)}").next_to(timp1, DOWN)
    timp3 = MathTex("\\text{Timpul 3: } 2 \\rightarrow 3 \\rightarrow 4 \\text{(doua procese)}").next_to(timp2, DOWN)
    timp4 = MathTex("\\text{Timpul 4: } 4 \\rightarrow 1 \\rightarrow 0 \\text{(doua procese)}").next_to(timp3, DOWN)

    self.play(Write(timp1))
    self.wait(3)
    self.play(Write(timp2))
    self.wait(3)
    self.play(Write(timp3))
    self.wait(3)
    self.play(Write(timp4))
    self.wait(3)


    pi1_t = SVGMobject("assets/PiCreature/PiCreatures_sassy.svg").move_to(pi1.get_center())
    pi2_t = SVGMobject("assets/PiCreature/PiCreatures_hooray.svg").move_to(pi2.get_center())
    pi3_t = SVGMobject("assets/PiCreature/PiCreatures_happy.svg").move_to(pi3.get_center())


    self.play(ReplacementTransform(pi1, pi1_t), ReplacementTransform(pi2, pi2_t), ReplacementTransform(pi3, pi3_t))
    self.wait(5)

    self.remove(
        *[mob for mob in self.mobjects]
    )




def de_ce(self : Scene):
    angrypi = SVGMobject("assets/PiCreature/PiCreatures_angry_yellow.svg").to_corner(DL)

    self.add((angrypi))
    angrypi_bubble =  ImageMobject("assets/PiCreature/Bubbles_speech_white.png").scale(0.5).next_to(angrypi, UP).shift(RIGHT*2.5)
    angrypi_speech = Tex("De ce mi-ar pasa?").scale(0.9).move_to(angrypi_bubble.get_center()).shift(UP*0.4)

    self.play(FadeIn(angrypi_bubble), Write(angrypi_speech))
    self.wait(6)
    self.remove(angrypi, angrypi_bubble, angrypi_speech)


    ec_stare = MathTex("P", "V", "=", "nR", "T").to_edge(UP)
    ec_stare2 = MathTex("\\frac{PV}{T}" "=", "nR").next_to(ec_stare, DOWN)
    self.play(Write(ec_stare))
    self.wait(2)
    self.play(ReplacementTransform(ec_stare.copy(), ec_stare2))
    self.wait(10)

    sq = SurroundingRectangle(ec_stare2, color=YELLOW)
    self.play(Create(sq))

    fie = Tex("Fie $P_i$, $V_i$, $T_i$ = parametrii initiali").next_to(sq, DOWN)
    fie2 = Tex("si $P_f$, $V_f$, $T_f$ = parametrii finali").next_to(fie, DOWN)
    self.play(Write(fie))
    self.play(Write(fie2))
    self.wait(5)

    ec1 = MathTex("\\frac{P_i V_i}{T_i} = nR")
    ec2 = MathTex("\\frac{P_f V_f}{T_f} = nR").next_to(ec1, DOWN)
    ecg = Group(ec1, ec2).to_corner(DL)
    self.play(Write(ec1), Write(ec2))
    self.wait(6)
    b = Brace(ecg, direction=RIGHT)
    ba = MathTex("\\Rightarrow").next_to(b, RIGHT)
    self.play(Write(b))
    self.play(Write(ba))

    final_ec  = MathTex("\\frac{P_i V_i}{T_i} = \\frac{P_f V_f}{T_f}").next_to(ba, RIGHT)
    self.play(Write(final_ec))
    self.wait(5)

    ba2 = MathTex("\\Rightarrow").next_to(final_ec, RIGHT)
    self.play(Write(ba2))
    fiecare = Tex("Procese termodinamice").next_to(ba2, RIGHT)
    self.play(Write(fiecare))
    self.wait(3)
    self.play(
        *[FadeOut(mob)for mob in self.mobjects]
    )

    final_ec2  = MathTex("\\frac{P_i V_i}{T_i} = \\frac{P_f V_f}{T_f}").to_edge(UP)
    self.play(Write(final_ec2))

    proces_izocor = Tex("Proces izocor (V - cst): ").to_edge(LEFT).shift(UP)
    proces_izocor_ec = MathTex("\\frac{P_i}{T_i} = \\frac{P_f}{T_f}").next_to(proces_izocor, RIGHT)
    self.play(Write(proces_izocor))
    self.wait(5)
    self.play(ReplacementTransform(final_ec2.copy(), proces_izocor_ec))
    self.wait(5)


    proces_izobar = Tex("Proces izobar (P - cst): ").to_edge(LEFT).shift(DOWN*0.5)
    proces_izobar_ec = MathTex("\\frac{V_i}{T_i} = \\frac{V_f}{T_f}").next_to(proces_izobar, RIGHT)
    self.play(Write(proces_izobar))
    self.wait(5)
    self.play(ReplacementTransform(final_ec2.copy(), proces_izobar_ec))
    self.wait(5)


    proces_izoterm = Tex("Proces izoterm (T - cst): ").to_edge(LEFT).shift(3*DOWN/1.5)
    proces_izoterm_ec = MathTex("P_i V_i = P_f V_f").next_to(proces_izoterm, RIGHT)
    self.play(Write(proces_izoterm))
    self.wait(5)
    self.play(ReplacementTransform(final_ec2.copy(), proces_izoterm_ec))
    self.wait(10)

    self.wait(10)
    final_izobar_ec2 = MathTex("\\Rightarrow \\frac{V}{T} = \\text{cst}", color=BLUE).next_to(proces_izobar_ec, RIGHT)
    final_izocor_ec2 = MathTex("\\Rightarrow \\frac{P}{T} = \\text{cst}", color=BLUE).next_to(proces_izocor_ec, RIGHT)
    final_izoterm_ec2 = MathTex("\\Rightarrow PV = \\text{cst}", color=BLUE).next_to(proces_izoterm_ec, RIGHT)
    self.play(Write(final_izobar_ec2), Write(final_izocor_ec2), Write(final_izoterm_ec2))

    self.wait(10)

    self.remove(
        *[mob for mob in self.mobjects]
    )

    pi = SVGMobject("assets/PiCreature/PiCreatures_pondering.svg").to_corner(DL)
    pi2 = SVGMobject("assets/PiCreature/PiCreatures_hooray.svg").to_corner(DL)
    pi2_bubble = ImageMobject("assets/PiCreature/Bubbles_speech_white.png").scale(0.3).next_to(pi2, UP).shift(RIGHT*2)
    pi2_speech = Paragraph("Putem considera ecuatiile", "niste functii implicite").scale(0.35).move_to(pi2_bubble).shift(UP*0.3)

    final_izocor_ec3 = MathTex("\\frac{P}{T} = \\text{cst}", color=BLUE).to_edge(UP)
    final_izobar_ec3 = MathTex("\\frac{V}{T} = \\text{cst}", color=BLUE).next_to(final_izocor_ec3, LEFT, buff=2)
    final_izoterm_ec3 = MathTex("PV = \\text{cst}", color=BLUE).next_to(final_izocor_ec3, RIGHT, buff=2)

    self.add(pi, final_izocor_ec3, final_izobar_ec3, final_izoterm_ec3)
    self.wait(5)
    self.play(FadeIn(pi2_bubble), Write(pi2_speech), ReplacementTransform(pi, pi2))


    self.wait(5)
    self.play(FadeOut(pi2_bubble), FadeOut(pi2_speech))
    explain_cst = Paragraph("cst poate fi orice valoare strict positiva", "mai mare ca 0 (daca cst <= 0 atunci n <= 0)", color=YELLOW).scale(0.7)
    self.play(Write(explain_cst))
    self.wait(10)
    final_izocor_ec4 = MathTex("\\frac{P}{T} = 1", color=BLUE).to_edge(UP)
    final_izobar_ec4 = MathTex("\\frac{V}{T} = 1", color=BLUE).next_to(final_izocor_ec3, LEFT, buff=2)
    final_izoterm_ec4 = MathTex("PV = 1", color=BLUE).next_to(final_izocor_ec3, RIGHT, buff=2)

    self.play(FadeOut(explain_cst), ReplacementTransform(final_izocor_ec3, final_izocor_ec4), ReplacementTransform(final_izobar_ec3, final_izobar_ec4), ReplacementTransform(final_izoterm_ec3, final_izoterm_ec4))
    
    pi3 = SVGMobject("assets/PiCreature/PiCreatures_pondering.svg").to_corner(DL)
    self.play(ReplacementTransform(pi2, pi3))

    np1 = NumberPlane(
        x_range=(-5, 5, 1),
        y_range=(-5, 5, 1),
        x_length=5,
        y_length=5,
        axis_config={"include_tip": True}
    ).to_edge(RIGHT).shift(DOWN*0.5)
    x_label = Tex("T").next_to(np1, RIGHT, buff=0).shift(LEFT*0.2+UP*0.5)
    y_label = Tex("V").next_to(np1, UP, buff=0).shift(RIGHT*0.4)
    self.play(final_izobar_ec4.animate.scale(1.5), final_izocor_ec4.animate.set_opacity(0.4), final_izoterm_ec4.animate.set_opacity(0.4), rate_func=rate_functions.ease_in_out_sine, run_time=0.5)
    self.play(Write(np1), Write(x_label), Write(y_label))
    func_np1 = ImplicitFunction(
            lambda x, y: x / y - 1,
            color=YELLOW,
            x_range = (-2.5,2.5),
            y_range = (-2.5, 2.5)
    ).move_to(np1.get_center())
    self.play(Write(func_np1))


    dotpos3 = ValueTracker(1)
    dotpos3_y = ValueTracker(1)
    is_manual = False
    point = Dot().move_to(np1.get_center() + dotpos3.get_value()*RIGHT + dotpos3.get_value()*UP)
    self.play(Create(point))

    coordonate = always_redraw(lambda: Tex(f"({dotpos3.get_value():.2f}, {dotpos3_y.get_value():.2f})", color=GREEN).scale(0.7).next_to(point, LEFT))

    self.play(Write(coordonate))

    def update_point(x, y):
        if not is_manual:
            x.move_to(np1.get_center() + dotpos3.get_value()*RIGHT + dotpos3.get_value()*UP)
            dotpos3_y.set_value(dotpos3.get_value())
        else:
            x.move_to(np1.get_center() + dotpos3.get_value()*RIGHT + y*UP)
            dotpos3_y.set_value(y)
    
    def check(x):
        if not is_manual:
            x.color = GREEN
        else:
            if dotpos3.get_value() != dotpos3_y.get_value():
                x.color = RED
            else:
                x.color = GREEN

    coordonate.add_updater(lambda x: check(x))
    ecuatie = always_redraw(lambda: MathTex("\\frac{%s}{%s} = {%s}" % (round(dotpos3.get_value(),2), round(dotpos3_y.get_value(),2), round(dotpos3.get_value()/dotpos3_y.get_value(), 2)), color=GREEN).scale(1.3).next_to(np1, LEFT, buff=1))
    ecuatie.add_updater(lambda x: check(x))
    self.play(Write(ecuatie))


    point.add_updater(lambda x: update_point(x, -1))
    self.play(dotpos3.animate.set_value(2), run_time = 1.5)
    self.wait(2)
    self.play(dotpos3.animate.set_value(-1), run_time = 3)
    self.wait(1)
    is_manual = True
    self.play(dotpos3.animate.set_value(2), run_time = 4)
    self.wait(1)
    self.play(dotpos3.animate.set_value(-1), run_time = 4)
    self.wait(2)

    self.play(final_izobar_ec4.animate.scale(2/3).set_opacity(0.4), final_izocor_ec4.animate.set_opacity(10/3).scale(1.5), rate_func=rate_functions.ease_in_out_sine, run_time=0.5)    
    self.wait(1)


    y_label2 = Tex("P").next_to(np1, UP, buff=0).shift(RIGHT*0.4)
    self.play(ReplacementTransform(y_label, y_label2))
    self.wait(5)

    self.play(final_izocor_ec4.animate.set_opacity(0.3).scale(2/3), final_izoterm_ec4.animate.scale(1.5).set_opacity(10/3), rate_func=rate_functions.ease_in_out_sine, run_time=0.5)    
    self.wait(1)

    x_label2 = Tex("V").next_to(np1, RIGHT, buff=0).shift(LEFT*0.2+UP*0.5)
    self.play(ReplacementTransform(x_label, x_label2), FadeOut(coordonate), FadeOut(point), FadeOut(ecuatie), FadeOut(func_np1))
    self.wait(1)

    func_np2 = ImplicitFunction(
            lambda x, y: x * y - 1,
            color=YELLOW,
            x_range = (-2.5,2.5),
            y_range = (-2.5, 2.5)
    ).move_to(np1.get_center())
    self.play(Write(func_np2))
    



    dotpos4 = ValueTracker(1)
    dotpos4_y = ValueTracker(1)
    is_manual = False
    point2 = Dot().move_to(np1.get_center() + dotpos4.get_value()*RIGHT + dotpos4_y.get_value()*UP)
    self.play(Create(point2))

    coordonate2 = always_redraw(lambda: Tex(f"({dotpos4.get_value():.2f}, {dotpos4_y.get_value():.2f})", color=GREEN).scale(0.7).next_to(point2, LEFT))

    self.play(Write(coordonate2))

    def update_point2(x, y):
        if not is_manual:
            dotpos4_y.set_value(1 / dotpos4.get_value())
            x.move_to(np1.get_center() + dotpos4.get_value()*RIGHT + dotpos4_y.get_value()*UP)
        else:
            x.move_to(np1.get_center() + dotpos4.get_value()*RIGHT + y*UP)
            dotpos4_y.set_value(y)
    
    def check2(x):
        if not is_manual:
            x.color = GREEN
        else:
            if dotpos4.get_value() != 1 / dotpos4_y.get_value():
                x.color = RED
            else:
                x.color = GREEN

    coordonate2.add_updater(lambda x: check2(x))
    ecuatie2 = always_redraw(lambda: MathTex(f"{dotpos4.get_value():.2f} \\cdot {dotpos4_y.get_value():.2f} = {(dotpos4.get_value() * dotpos4_y.get_value()):.2f}", color=GREEN).scale(1.3).next_to(np1, LEFT, buff=1))
    ecuatie2.add_updater(lambda x: check2(x))
    self.play(Write(ecuatie2))


    point2.add_updater(lambda x: update_point2(x, -0.67))
    self.play(dotpos4.animate.set_value(2), run_time = 2)
    self.wait(1)
    self.play(dotpos4.animate.set_value(-1.5), run_time=3)
    self.wait(3)
    is_manual = True
    self.play(dotpos4.animate.set_value(0.5), run_time=3)
    self.wait(5)

    self.remove(
        *[mob for mob in self.mobjects]
    )







def functii_implicite(self : Scene):
    intrebare = Paragraph("De ce procesele izocore si izobare sunt functii liniare?", "De ce procesul izoterm nu este?").scale(0.8).to_edge(UP)
    self.play(Write(intrebare), run_time=3)

    np1 = NumberPlane(
        x_range=(-4, 4, 1),
        y_range=(-4, 4, 1),
        x_length=4,
        y_length=4,
    ).shift(LEFT * 3 + DOWN)
    np2 = NumberPlane(
        x_range=(-4, 4, 1),
        y_range=(-4, 4, 1),
        x_length=4,
        y_length=4,
    ).shift(RIGHT * 3 + DOWN)

    izocor_izobar = Tex("izocor, izobar").scale(0.8).next_to(np1, UP)
    izoterm = Tex("izoterm").scale(0.8).next_to(np2, UP)

    self.play(Write(np1), Write(np2), Write(izocor_izobar), Write(izoterm))
    self.wait(3)

    g1 = np1.plot(lambda x: x, (0, 4), color=YELLOW)
    g2 = np2.plot(lambda x: 1/x, (0.25, 4), color=YELLOW)
    self.play(Create(g1))
    self.play(Create(g2))

    self.wait(3)
    self.remove(np1, np2, izocor_izobar, izoterm, intrebare, g1, g2)


    ec = MathTex("x + y = 0").to_edge(UP)
    pi = SVGMobject("assets/PiCreature/PiCreatures_happy.svg").to_corner(DL)
    self.add(ec, pi)
    self.wait(5)

    sol1 = MathTex("(0, 0)").next_to(ec, DOWN)
    sol2 = MathTex("(2, -2)").next_to(sol1, DOWN)
    sol3 = MathTex("(-1.5, 1.5)").next_to(sol2, DOWN)
    sol4 = MathTex("\\cdots").next_to(sol3, DOWN)

    self.play(Write(sol1))
    self.play(Write(sol2))
    self.play(Write(sol3))
    self.play(Write(sol4))
    ec_g = VGroup(ec, sol1, sol2, sol3, sol4)
    self.wait()

    pi2 = SVGMobject("assets/PiCreature/PiCreatures_speaking.svg").move_to(pi.get_center())
    pi2_bubble =  ImageMobject("assets/PiCreature/Bubbles_speech_white.png").scale(0.4).next_to(pi, UP).shift(RIGHT*2.2)
    pi2_speech = Paragraph("Putem crea o functie",  "cu aceste valori!").scale(0.5).move_to(pi2_bubble.get_center()).shift(UP*0.4)
    pi3 = SVGMobject("assets/PiCreature/PiCreatures_thinking.svg").move_to(pi.get_center())

    self.play(ReplacementTransform(pi, pi2), FadeIn(pi2_bubble), Write(pi2_speech))
    self.wait(5)
    self.play(FadeOut(pi2_bubble), FadeOut(pi2_speech), ReplacementTransform(pi2, pi3))
    self.play(ec_g.animate.to_corner(UL))
    self.play(FadeOut(sol1), FadeOut(sol2), FadeOut(sol3), FadeOut(sol4))

    np3 = NumberPlane(
        x_range=(-5, 5, 1),
        y_range=(-5, 5, 1),
        x_length=5,
        y_length=5,
        axis_config={"include_tip": True}
    ).to_edge(RIGHT)
    x_label = np3.get_x_axis_label("x")
    y_label = np3.get_y_axis_label("y")
    self.play(Write(np3), Write(x_label), Write(y_label))

    func_np3 = ImplicitFunction(
            lambda x, y: x + y,
            color=YELLOW,
            x_range = (-2.5,2.5),
            y_range = (-2.5, 2.5)
    ).move_to(np3.get_center())
    self.play(Create(func_np3))

    global dotpos2
    dotpos2 = ValueTracker(0.00)
    is_manual = False
    global dotpos_y_manual2
    dotpos_y_manual2 = ValueTracker(0.00)


    def move_to(x, m, ym):
        global dotpos_y_manual2
        if m == False:
            x.move_to(np3.get_center() + dotpos2.get_value()*RIGHT + -1*dotpos2.get_value()*UP)
            dotpos_y_manual2.set_value(-1*dotpos2.get_value())
        else:
            dotpos_y_manual2.set_value(ym)
            x.move_to(np3.get_center() + dotpos2.get_value()*RIGHT + ym*UP)

    def check_correct(x):
        global dotpos2
        global dotpos_y_manual2
        if is_manual == False:
            x.color = GREEN
        else:
            if round(dotpos2.get_value()+dotpos_y_manual2.get_value(), 2) == 0:
                x.color = GREEN
            else:
                x.color = RED


    point = Dot(np3.get_center(),color=WHITE)
    


    coordonate = always_redraw(lambda: Tex(f"({dotpos2.get_value():.2f}, {dotpos_y_manual2.get_value():.2f})", color=GREEN).scale(0.7))
    coordonate.add_updater(lambda x : x.next_to(point, LEFT))
    coordonate.add_updater(lambda x: check_correct(x))
    point.add_updater(lambda x: move_to(x, False, 0))

    ecuatie = always_redraw(lambda: MathTex(f"{dotpos2.get_value():.2f} + {dotpos_y_manual2.get_value():.2f} = {(dotpos2.get_value()+dotpos_y_manual2.get_value()):.2f}", color=GREEN).scale(1.3).next_to(np3, LEFT, buff=1))
    ecuatie.add_updater(lambda x: check_correct(x))
    
    self.play(Create(point))
    self.add(coordonate, ecuatie)
    self.play(dotpos2.animate.set_value(-2), run_time=5)
    self.wait()
    self.play(dotpos2.animate.set_value(1.5), run_time=4)
    point.remove_updater(lambda x: move_to(x, False, 0))
    point.add_updater(lambda x: move_to(x, True, -1.5))
    is_manual = True
    self.play(dotpos2.animate.set_value(-1), run_time=2)
    self.wait(5)
    self.play(dotpos2.animate.set_value(1.5), run_time=2)

    self.wait(5)
    fi = Tex("Functie implicita", color=YELLOW).to_edge(UP)
    self.play(Write(fi))
    self.wait(7)
    self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

    de_ce(self)
    

def capitolul1(self : Scene):
    titlu = Tex("Capitolul 1: Functionarea motorului diesel").scale(1.2)
    self.play(Write(titlu))

    self.wait()
    self.remove(titlu)

    m = 1.5
    n = 0.7

    dashline = DashedLine(n*LEFT+m*UP, m*UP, dash_length=n)
    dashline2 = DashedLine(m*UP, n*RIGHT+m*UP, dash_length=n)

    line_t = Line(n*LEFT+m*UP, m*UP)
    line_t2 = Line(m*UP, n*RIGHT+m*UP)

    
    injector = Line(UP*0.3, DOWN*0.3).next_to(line_t, RIGHT, buff=0).shift(UP*0.15)

    line1 = Line(n*LEFT + m * UP, n*LEFT + m * DOWN)
    line3 = Line(n*RIGHT+m*DOWN, n*RIGHT+m*UP)
    plot = VGroup(line1, line3, line_t, line_t2, injector, dashline, dashline2)
    circle = Line(n*LEFT + m * DOWN, n*RIGHT+m*DOWN)
    circle.set_path_arc(5)
    point = Dot(radius = 0.1, color=WHITE).move_to(circle.get_center())
    
    plot.add(circle, point)




    circ = Circle(radius=0.6, stroke_opacity=0).move_to(point.get_center())
    dotpos = ValueTracker(PI/2)
    dot1 = always_redraw(lambda:
        Dot().move_to(circ.point_at_angle(dotpos.get_value()))
    )

    lineLength = 2.4
    dot2 = Dot(fill_opacity=1)
    dot2 = always_redraw(lambda:
        dot2.move_to(
            [0, dot1.get_center()[1]+np.sqrt(lineLength**2 - dot1.get_center()[0]**2), 0]
        )
    )


    piston= Rectangle(height=0.6, width = 2*n).next_to(dot2, UP, buff=0)

    line = always_redraw(lambda:
        Line(dot1.get_center(), dot2.get_center())
    )
    plot.add(dot1, dot2, circ, line, piston)
    piston = always_redraw(lambda : piston.next_to(dot2, UP, buff=0))
 
    plot.shift(UP*0.75)
    self.play(FadeIn(plot))



    def update_line_t(x):
        if (dotpos.get_value() / PI) % 4 > 1/2 and (dotpos.get_value() / PI) % 4 <= 3/2:
            x.set_opacity(0)
        else:
            x.set_opacity(1)
    def update_dashed_for_line_t(z):
        if (dotpos.get_value() / PI) % 4 > 1/2 and (dotpos.get_value() / PI) % 4 <= 3/2:
            z.set_opacity(1)
        else:
            z.set_opacity(0)

    def update_line_t2(x):
        if (dotpos.get_value() / PI - 0.5) % 4 > 3 and (dotpos.get_value() / PI - 0.5) % 4< 4:
            x.set_opacity(0)
        else:
            x.set_opacity(1)
    def update_dashed_for_line_t2(z):
        if (dotpos.get_value() / PI - 0.5) % 4 > 3 and (dotpos.get_value() / PI - 0.5) % 4 < 4:
            z.set_opacity(1)
        else:
            z.set_opacity(0)
    def update_injector(x):
        if (dotpos.get_value() /PI) % 4 > 5/2 and (dotpos.get_value() /PI) % 4 < 2.8:
            x.set_color(RED)
        else:
            x.set_color(WHITE)


    line_t.add_updater(update_line_t)
    self.add(dashline)
    dashline.add_updater(update_dashed_for_line_t)
    line_t2.add_updater(update_line_t2)
    self.add(dashline2)
    dashline2.add_updater(update_dashed_for_line_t2)
    injector.add_updater(update_injector)


    self.wait(4)

    arrow_cilindru = Arrow(LEFT*5, LEFT)
    arrow_cilindru_text = Tex("cilindru").next_to(arrow_cilindru, UP, buff=0)
    self.play(Create(arrow_cilindru), Write(arrow_cilindru_text))
    self.wait(5)

    arrow_camera = Arrow(LEFT*5, LEFT).next_to(piston, LEFT, buff=0.3).shift(UP*0.5)
    arrow_camera_text = Tex("camera de ardere").next_to(arrow_camera, UP, buff=0.1)
    self.play(Create(arrow_camera), Write(arrow_camera_text))
    self.wait(5)

    arrow_injector = Arrow(RIGHT*5, RIGHT).next_to(injector, RIGHT, buff=0.3).shift(UP*0.1)
    arrow_injector_text = Tex("injector").next_to(arrow_injector, UP, buff=0)
    self.play(Create(arrow_injector), Write(arrow_injector_text))
    self.wait(5)

    arrow_piston = Arrow(RIGHT*5, 0*RIGHT)
    arrow_piston_text = Tex("piston").next_to(arrow_piston, UP, buff=0)
    self.play(Create(arrow_piston), Write(arrow_piston_text))
    self.wait(5)
    arrows = VGroup(arrow_cilindru, arrow_cilindru_text, arrow_injector, arrow_injector_text, arrow_camera, arrow_camera_text, arrow_piston, arrow_piston_text)


    self.play(FadeOut(arrows))

    arrow_supapa_admisie = Arrow(LEFT*5, LEFT).next_to(piston, LEFT, buff=0.3).shift(UP*0.65)
    arrow_supapa_admisie_text = Tex("supapa de admisie").next_to(arrow_supapa_admisie, UP, buff=0)
    self.play(FadeIn(arrow_supapa_admisie), Write(arrow_supapa_admisie_text))
    self.wait(5)

    arrow_supapa_evacuare = Arrow(RIGHT*5, RIGHT).next_to(piston, RIGHT, buff=0.3).shift(UP*0.65)
    arrow_supapa_evacuare_text = Tex("supapa de evacuare").next_to(arrow_supapa_evacuare, UP, buff=0)
    self.play(FadeIn(arrow_supapa_evacuare), Write(arrow_supapa_evacuare_text))

    self.wait(10)
    self.play(FadeOut(arrow_supapa_admisie), FadeOut(arrow_supapa_admisie_text), FadeOut(arrow_supapa_evacuare), FadeOut(arrow_supapa_evacuare_text))
    self.wait(6)
    self.play(dotpos.animate.set_value((2*PI + PI/2)*2 - PI/2), rate_func=rate_functions.smoothstep, run_time=10)
    dotpos = ValueTracker(PI/2)

    self.wait()

    timp1 = Tex("Primul timp").next_to(plot, LEFT, buff=1.5)
    timp2 = Tex("Al doilea timp").next_to(plot, LEFT, buff=1.5)
    timp3 = Tex("Al treilea timp").next_to(plot, LEFT, buff=1.5)
    timp4 = Tex("Al patrulea timp").next_to(plot, LEFT, buff=1.5)

    self.play(Write(timp1))
    self.play(dotpos.animate.set_value((3*PI/2)), rate_func=rate_functions.smoothstep, run_time=5)
    self.wait(5)
    self.play(FadeOut(timp1))
    self.play(Write(timp2))
    self.play(dotpos.animate.set_value((5*PI/2)), rate_func=rate_functions.smoothstep, run_time=5)
    self.wait(5)
    self.play(FadeOut(timp2))
    self.play(Write(timp3))
    self.play(dotpos.animate.set_value((7*PI/2)), rate_func=rate_functions.smoothstep, run_time=8)
    self.wait(5)
    self.play(FadeOut(timp3))
    self.play(Write(timp4))
    self.play(dotpos.animate.set_value((9*PI/2)), rate_func=rate_functions.smoothstep, run_time=5)
    self.wait(5)
    self.play(FadeOut(timp4))
    dotpos = ValueTracker(PI/2)
    self.play(dotpos.animate.set_value((2*PI + PI/2)*2 - PI/2), rate_func=rate_functions.smoothstep, run_time=2.5)
    dotpos = ValueTracker(PI/2)
    self.play(dotpos.animate.set_value((2*PI + PI/2)*2 - PI/2), rate_func=rate_functions.smoothstep, run_time=2.5)
    self.wait(10)
    self.remove(line_t, line_t2, injector, circ, circle, dashline, dashline2, dot1, dot2, line1, line3, point, piston, line)

    observa_ce_nu_spun(self)
    functii_implicite(self)



def capitolul3(self : Scene):
    cap3 = Tex("Capitolul 3: Eficienta motorului Diesel").scale(1.2)
    self.play(Write(cap3))
    self.wait(4)
    self.remove(cap3)

    pi1 = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").to_corner(DL)
    pi2 = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").next_to(pi1, RIGHT)
    pi3 = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").next_to(pi2, RIGHT)
    pi_teacher = SVGMobject("assets/PiCreature/plain_teacher.svg").scale(1.2).to_corner(DR)
    ef = Tex("Eficienta").to_edge(UP)

    self.add(pi1, pi2, pi3, pi_teacher, ef)

    pi3_ask = SVGMobject("assets/PiCreature/PiCreatures_raise_left_hand.svg").move_to(pi3.get_center())
    pi3_bubble =  ImageMobject("assets/PiCreature/Bubbles_speech_white.png").scale(0.4).next_to(pi3_ask, UP).shift(RIGHT*2.2)
    pi3_speech = Tex("Ce e mai exact eficienta?").scale(0.7).move_to(pi3_bubble.get_center()).shift(UP*0.4)

    self.wait(2)
    self.play(ReplacementTransform(pi3, pi3_ask), FadeIn(pi3_bubble), Write(pi3_speech))
    self.wait(1)

    motor_termic = Circle().next_to(ef, DOWN, buff=1)
    qh = MathTex("\\overset{1000J}{\\rightarrow}").scale(1.3).next_to(motor_termic, LEFT)
    qc = MathTex("\\overset{500J}{\\rightarrow}").scale(1.3).next_to(motor_termic, RIGHT)

    pi3_t = SVGMobject("assets/PiCreature/PiCreatures_plain.svg").move_to(pi3.get_center())
    self.play(FadeOut(pi3_bubble), FadeOut(pi3_speech), ReplacementTransform(pi3_ask, pi3_t))

    self.play(Create(motor_termic), Write(qh), Write(qc))

    pi_teacher_speaking =  SVGMobject("assets/PiCreature/PiCreatures_speaking_teacher.svg").scale(1.2).move_to(pi_teacher.get_center())
    pi_teacher_bubble = ImageMobject("assets/PiCreature/Bubbles_speech_white_flip.png").scale(0.3).next_to(pi_teacher, UP).shift(LEFT*1.5)
    pi_teacher_speech = Paragraph("Care credeti ca e", "eficienta acestui motor?").scale(0.35).move_to(pi_teacher_bubble.get_center()).shift(UP*0.3)
    self.play(ReplacementTransform(pi_teacher, pi_teacher_speaking), FadeIn(pi_teacher_bubble), Write(pi_teacher_speech))
    self.wait(3)

    pi1_ask = SVGMobject("assets/PiCreature/PiCreatures_hooray.svg").move_to(pi1.get_center())
    pi1_bubble =  ImageMobject("assets/PiCreature/Bubbles_speech_white.png").scale(0.3).next_to(pi1_ask, UP).shift(RIGHT*2.2)
    pi1_speech = Tex("Eficienta 50\%!").scale(0.6).move_to(pi1_bubble.get_center()).shift(UP*0.3)

    self.play(ReplacementTransform(pi1, pi1_ask), FadeIn(pi1_bubble), Write(pi1_speech))


    self.wait(3)
    self.remove(*[(mob) for mob in self.mobjects])

    motor_termic2 = Circle()
    qp = MathTex("\\overset{1000J}{\\rightarrow}").scale(1.3).next_to(motor_termic2, LEFT)
    qp_text = MathTex("Q_p").next_to(qp, LEFT)
    l = MathTex("\\overset{500J}{\\rightarrow}").scale(1.3).next_to(motor_termic2, RIGHT)
    l_text = MathTex("L").next_to(l, RIGHT)
    expl_qp = Tex("Energie termica adaugata").scale(0.7).next_to(qp, DOWN).shift(LEFT*1.5)
    expl_l = Tex("Lucru mecanic folositor").scale(0.7).next_to(l, DOWN).shift(RIGHT*1.25)
    sageata = MathTex("\\rightarrow").rotate(3*PI/2).next_to(motor_termic2, DOWN)
    qc = MathTex("500J").next_to(sageata, RIGHT)
    expl_qc = Tex("Energie pierduta").scale(0.7).next_to(sageata, DOWN)
    qc_text = MathTex("Q_c").next_to(expl_qc, DOWN)


    self.play(Create(motor_termic2), Write(qp), Write(l), Write(qp_text), Write(l_text))
    self.wait()
    self.play(Write(expl_qp))
    self.wait(4)
    self.play(Write(expl_l))
    self.wait(4)
    self.play(Write(sageata), Write(qc), Write(expl_qc), Write(qc_text))
    self.wait(4)


    ec = MathTex("\\eta = \\frac{L}{Q_p}").to_corner(UL)
    ec2 = MathTex("= \\frac{Q_p - Q_c}{Q_p}").next_to(ec, RIGHT)
    ec3 = MathTex("= \\frac{Q_p}{Q_p} - \\frac{Q_c}{Q_p}").next_to(ec2, RIGHT)
    ec4 = MathTex("= 1 - \\frac{Q_c}{Q_p}").next_to(ec3, RIGHT)

    self.play(Write(ec))
    self.wait(5)
    self.play(Write(ec2))
    self.wait(5)
    self.play(Write(ec3))
    self.wait(5)
    self.play(Write(ec4))
    self.wait(5)
    self.remove(*[(mob) for mob in self.mobjects])




def capitolul2(self : Scene):
    cap2 = Tex("Capitolul 2: Ciclul motorului Diesel").scale(1.2)
    self.play(Write(cap2))
    self.wait(5)
    self.remove(cap2)

    number_plane = NumberPlane()
    self.play(Write(number_plane))

    numberplane = NumberPlane(
        x_range=(-30, 30, 1),
        y_range=(-30, 30, 1),
        x_length=60,
        y_length=60,
    )
    self.add(numberplane)
    self.remove(number_plane)

    self.wait()
    presiunea_Oy = Tex("P").to_edge(UP).shift(LEFT*0.5)
    volumul_Ox = Tex("V").to_edge(RIGHT).shift(UP*0.5)
    self.play(Write(presiunea_Oy), Write(volumul_Ox))
    self.wait(3)
    self.play(Unwrite(presiunea_Oy), Unwrite(volumul_Ox))

    self.play(numberplane.animate.shift(LEFT*5.5 + DOWN*3).scale(0.8), run_time=2)
    self.wait(1)




    m = 1
    n = 14/30

    dashline = DashedLine(n*LEFT+m*UP, m*UP, dash_length=n)
    dashline2 = DashedLine(m*UP, n*RIGHT+m*UP, dash_length=n)

    line_t = Line(n*LEFT+m*UP, m*UP)
    line_t2 = Line(m*UP, n*RIGHT+m*UP)

    
    injector = Line(UP*0.2, DOWN*0.2).next_to(line_t, RIGHT, buff=0).shift(UP*1/15)

    line1 = Line(n*LEFT + m * UP, n*LEFT + m * DOWN)
    line3 = Line(n*RIGHT+m*DOWN, n*RIGHT+m*UP)
    plot = VGroup(line1, line3, line_t, line_t2, injector, dashline, dashline2)
    circle = Line(n*LEFT + m * DOWN, n*RIGHT+m*DOWN)
    circle.set_path_arc(5)
    point = Dot(radius = 1/15, color=WHITE).move_to(circle.get_center())
    
    plot.add(circle, point)




    circ = Circle(radius=6/15, stroke_opacity=0).move_to(point.get_center())
    dotpos5 = ValueTracker(PI/2)
    dot1 = Dot(radius=8/150).move_to(circ.point_at_angle(dotpos5.get_value()))
    dot1 = always_redraw(lambda:
        dot1.move_to(circ.point_at_angle(dotpos5.get_value()))
    )

    lineLength = 23/15
    dot2 = Dot(fill_opacity=1, radius=8/150)
    dot2 = always_redraw(lambda:
        dot2.move_to(
            [dot2.get_center()[0], (dot1.get_center()[1])+np.sqrt(abs(lineLength**2 - (dot1.get_center()[0] - point.get_center()[0])**2)), 0]
        )
    )


    piston= Rectangle(height=6/15, width = 2*n).next_to(dot2, UP, buff=0)

    line = always_redraw(lambda:
        Line(dot1.get_center(), dot2.get_center())
    )
    plot.add(dot1, dot2, circ, line, piston)
    piston = always_redraw(lambda : piston.next_to(dot2, UP, buff=0))
 
    plot.to_corner(UR, buff=0.6)
    plot.set_z_index = 10
    
    sq = Rectangle(height = 4, width = 4, stroke_color=YELLOW, color=BLACK, fill_opacity=1).move_to(plot.get_center()).shift(0.8*LEFT)
    sq.set_z_index = 9
    timp1 = Tex("Timp: 1").next_to(plot, LEFT, buff=0.1).shift(UP)
    timp2 = Tex("Timp: 2").next_to(plot, LEFT, buff=0.1).shift(UP)
    timp3 = Tex("Timp: 3").next_to(plot, LEFT, buff=0.1).shift(UP)
    timp4 = Tex("Timp: 4").next_to(plot, LEFT, buff=0.1).shift(UP)
    pr01 = MathTex("0 \\rightarrow 1").scale(0.5).next_to(timp1, DOWN)
    pr12 = MathTex("1 \\rightarrow 2").scale(0.5).next_to(timp2, DOWN)
    pr23 = MathTex("2 \\rightarrow 3").scale(0.5).next_to(timp3, DOWN)
    pr34 = MathTex("3 \\rightarrow 4").scale(0.5).next_to(pr23, DOWN)
    pr41 = MathTex("4 \\rightarrow 1").scale(0.5).next_to(timp4, DOWN)
    pr10 = MathTex("1 \\rightarrow 0").scale(0.5).next_to(pr41, DOWN)


    self.play(Create(sq))
    self.play(FadeIn(plot), Write(timp1))



    def update_line_t(x):
        if (dotpos5.get_value() / PI) % 4 > 1/2 and (dotpos5.get_value() / PI) % 4 <= 3/2:
            x.set_opacity(0)
        else:
            x.set_opacity(1)
    def update_dashed_for_line_t(z):
        if (dotpos5.get_value() / PI) % 4 > 1/2 and (dotpos5.get_value() / PI) % 4 <= 3/2:
            z.set_opacity(1)
        else:
            z.set_opacity(0)

    def update_line_t2(x):
        if (dotpos5.get_value() / PI - 0.5) % 4 > 3 and (dotpos5.get_value() / PI - 0.5) % 4< 4:
            x.set_opacity(0)
        else:
            x.set_opacity(1)
    def update_dashed_for_line_t2(z):
        if (dotpos5.get_value() / PI - 0.5) % 4 > 3 and (dotpos5.get_value() / PI - 0.5) % 4 < 4:
            z.set_opacity(1)
        else:
            z.set_opacity(0)
    def update_injector(x):
        if (dotpos5.get_value() /PI) % 4 > 5/2 and (dotpos5.get_value() /PI) % 4 < 2.8:
            x.set_color(RED)
        else:
            x.set_color(WHITE)


    line_t.add_updater(update_line_t)
    self.add(dashline)
    dashline.add_updater(update_dashed_for_line_t)
    line_t2.add_updater(update_line_t2)
    self.add(dashline2)
    dashline2.add_updater(update_dashed_for_line_t2)
    injector.add_updater(update_injector)

    self.play(dotpos5.animate.set_value(3*PI/2),  rate_func=rate_functions.smoothstep ,run_time=5)


    p0 = Dot(4*LEFT+2.2*DOWN)
    point1 = Dot(2*RIGHT+2.2*DOWN)
    point2 = Dot(4*LEFT + 2*UP)
    point3 = Dot(2*UP + 1.5*LEFT)
    point4 = Dot(2*RIGHT + 0.5*DOWN)
    line0_1 = Line(p0.get_center(), point1.get_center())
    line1_2 = Line(start=point1.get_center(), end=point2.get_center())
    line2_3 = Line(start=point2.get_center(), end=point3.get_center())
    line3_4 = Line(start=point3.get_center(), end=point4.get_center())
    line4_1 = Line(start=point4.get_center(), end=point1.get_center())
    line1_0 = Line(start=point1.get_center(), end=p0.get_center(), color=RED)

    line1_2.set_path_arc(-1)
    line3_4.set_path_arc(0.7)

    number0 = Tex("0").next_to(p0, UP).shift(LEFT*0.2)
    number1 = Tex("1").next_to(point1, RIGHT)
    number2 = Tex("2").next_to(point2, UP)
    number3 = Tex("3").next_to(point3, UP)
    number4 = Tex("4").next_to(point4, RIGHT)


    self.wait()
    self.play(
        Create(p0), Create(point1), Create(line0_1), Create(number0), Create(number1), run_time=1
    )
    self.play(Write(pr01), run_time=0.5)

    l0 = DashedLine(p0.get_center(), (p0.get_center()[0]*RIGHT - 3*UP), color=GREEN)
    l0_2 = DashedLine(p0.get_center(), (p0.get_center()[1]*UP - 5.5*RIGHT), color=GREEN)
    v0 = MathTex("V_0").next_to(l0, DOWN).scale(0.8)
    p0 = MathTex("P_0").next_to(l0_2, LEFT).scale(0.8)
    self.play(Write(l0), Write(l0_2), run_time=0.5)
    self.play(Write(v0), Write(p0))
    self.wait(8)

    l1 = DashedLine(point1.get_center(), (point1.get_center()[0]*RIGHT - 3* UP), color=GREEN)
    v1 = MathTex("V_1").next_to(l1, DOWN).scale(0.8)
    p01 = MathTex("P_0 = P_1").next_to(l0_2, LEFT, buff=0).scale(0.8)
    self.play(Write(l1), run_time=0.5)
    self.play(Write(v1), ReplacementTransform(p0, p01))
    self.wait(5)

    self.play(ReplacementTransform(timp1, timp2), FadeOut(pr01))
    self.play(dotpos5.animate.set_value(2*PI + PI/2),  rate_func=rate_functions.smoothstep ,run_time=5)
    self.wait()
    self.play(
        Create(point2), Create(line1_2), Create(number2), run_time=1
    )
    self.play(Write(pr12), run_time=0.5)

    l2 = DashedLine(point2.get_center(), (point2.get_center()[0]*RIGHT - 2.2*UP), color=GREEN)
    l2_2 = DashedLine(point2.get_center(), (point2.get_center()[1]*UP - 5.5*RIGHT), color=GREEN)
    v02 = MathTex("V_0 = V_2").next_to(l0, DOWN).scale(0.8)
    p2 = MathTex("P_2").next_to(l2_2, LEFT).scale(0.8)
    self.play(Write(l2), Write(l2_2), run_time=0.5)
    self.play(ReplacementTransform(v0, v02), Write(p2))
    self.wait(8)



    self.play(ReplacementTransform(timp2, timp3), FadeOut(pr12))
    self.play(dotpos5.animate.set_value(2*PI + 3*PI/4),  rate_func=rate_functions.smoothstep ,run_time=1.5)
    self.wait()
    self.play(
        Create(point3), Create(line2_3), Create(number3), run_time=1
    )
    self.play(Write(pr23), run_time=0.5)
    
    l3 = DashedLine(point3.get_center(), (point3.get_center()[0]*RIGHT - 3*UP), color=GREEN)
    p23 = MathTex("P_2 = P_3").next_to(l2_2, LEFT, buff=0).scale(0.8)
    v3 = MathTex("V_3").next_to(l3, DOWN).scale(0.8)
    self.play(Write(l3))
    self.play(ReplacementTransform(p2, p23), Write(v3))
    self.wait(8)

    self.play(dotpos5.animate.set_value(3*PI + PI/2),  rate_func=rate_functions.smoothstep ,run_time=3)
    self.wait()
    self.play(
        Create(point4), Create(line3_4), Create(number4), run_time=1
    )
    self.play(Write(pr34), run_time=0.5)

    l4 = DashedLine(point4.get_center(), point1.get_center(), color=GREEN)
    l4_2 = DashedLine(point4.get_center(),  (point4.get_center()[1]*UP - 5.5*RIGHT), color=GREEN)
    v14 = MathTex("V_1 = V_4").next_to(l1, DOWN).scale(0.8)
    p4 = MathTex("P_4").next_to(l4_2, LEFT).scale(0.8)

    self.play(Write(l4), Write(l4_2))
    self.play(Write(p4), ReplacementTransform(v1, v14))
    self.wait(8)

    self.play(ReplacementTransform(timp3, timp4), FadeOut(pr23), FadeOut(pr34))
    self.play(dotpos5.animate.set_value(3*PI + PI/2+0.01), rate_func=rate_functions.smoothstep ,run_time=0.1)
    self.wait()
    self.play(
        FadeOut(l4),
        Create(line4_1), run_time=1
    )
    self.play(Write(pr41), run_time=0.5)
    self.wait(8)

    self.play(dotpos5.animate.set_value(4*PI+PI/2),  rate_func=rate_functions.smoothstep ,run_time=5)
    self.wait()

    self.play(Create(line1_0), run_time=1)
    self.play(Write(pr10), run_time=0.5)
    self.wait(10)

    group = Group()
    for mob in self.mobjects:
        group.add(*mob)
    #self.remove(*[(mob) for mob in self.mobjects])

    self.play(FadeOut(group), run_time=0)

    observa_ce_nu_spun2(self)

    #capitolul3

    capitolul3(self)


    dotpos5.set_value(2*PI + PI/2)
    self.play(FadeIn(group), FadeOut(timp4), FadeOut(pr41), FadeOut(pr10), run_time=0)
    self.wait(3)

    qh = MathTex("Q_p").next_to(line2_3, UP)
    qh_f = MathTex("Q_p = c_P m (T_3 - T_2)").scale(0.8).next_to(line2_3, UP, buff=1)
    self.wait(5)
    self.play(Write(qh))
    self.wait(1)
    self.play(dotpos5.animate.set_value(2*PI + PI/2 + PI/4), rate_func=rate_functions.smoothstep ,run_time=3)
    self.wait(5)
    self.play(ReplacementTransform(qh, qh_f))
    self.wait(10)


    qc = MathTex("Q_c").next_to(line4_1, RIGHT)
    qc_f = MathTex("Q_c = c_V m (T_4 - T_1)").scale(0.8).next_to(line4_1, RIGHT)
    self.play(Write(qc))
    self.wait(1)
    self.play(dotpos5.animate.set_value(2*PI + 3*PI/2+0.00001), rate_func=rate_functions.smoothstep ,run_time=1.5)
    self.wait(7)
    self.play(ReplacementTransform(qc, qc_f))
    self.wait(15)
    self.remove(*[(mob) for mob in self.mobjects])

    ec = MathTex("\\eta = \\frac{L}{Q_p}").to_corner(UL)
    ec2 = MathTex("= \\frac{Q_p - Q_c}{Q_p}").next_to(ec, RIGHT)
    ec3 = MathTex("= \\frac{Q_p}{Q_p} - \\frac{Q_c}{Q_p}").next_to(ec2, RIGHT)
    ec4 = MathTex("= 1 - \\frac{Q_c}{Q_p}").next_to(ec3, RIGHT)
    ec5 = MathTex("= 1 - \\frac{c_V (T_4 - T_1)}{c_P (T_3 - T_2)}").next_to(ec4, RIGHT)

    motor_termic2 = Circle()
    qp = MathTex("\\overset{1000J}{\\rightarrow}").scale(1.3).next_to(motor_termic2, LEFT)
    qp_text = MathTex("Q_p").next_to(qp, LEFT)
    l = MathTex("\\overset{500J}{\\rightarrow}").scale(1.3).next_to(motor_termic2, RIGHT)
    l_text = MathTex("L").next_to(l, RIGHT)
    expl_qp = Tex("Energie termica adaugata").scale(0.7).next_to(qp, DOWN).shift(LEFT*1.5)
    expl_l = Tex("Lucru mecanic folositor").scale(0.7).next_to(l, DOWN).shift(RIGHT*1.25)
    sageata = MathTex("\\rightarrow").rotate(3*PI/2).next_to(motor_termic2, DOWN)
    qc = MathTex("500J").next_to(sageata, RIGHT)
    expl_qc = Tex("Energia termica pirduta").scale(0.7).next_to(sageata, DOWN)
    qc_text = MathTex("Q_c").next_to(expl_qc, DOWN)

    self.add(ec,ec2,ec3,ec4, motor_termic2, qp, qp_text, l, l_text, expl_qp, expl_l, sageata, qc, qc_text, expl_qc)
    self.wait(2)
    self.play(Write(ec5))
    self.wait(12)
    self.remove(*[(mob) for mob in self.mobjects])


    p1 = SVGMobject("assets/PiCreature/PiCreatures_pondering.svg").to_corner(DL)
    p2 = SVGMobject("assets/PiCreature/PiCreatures_hooray.svg").to_corner(DL)
    g = MathTex("\\gamma = \\frac{c_V}{c_P}").to_edge(UP)
    self.add(p1)
    self.play(Write(g))
    ec6 = MathTex("\\eta = 1 - \\gamma \\frac{T_4 - T_1}{T_3 - T_2}").next_to(g, DOWN)
    self.wait(5)
    self.play(Write(ec6))
    s = SurroundingRectangle(ec6, color=YELLOW)
    self.play(Create(s), ReplacementTransform(p1, p2))

    self.wait(12)

    self.remove(*[(mob) for mob in self.mobjects])



def capitolul4(self : Scene):
    cap4 = Tex("Capitolul 4: Istoria Motorului Diesel").scale(1.2)
    self.play(Write(cap4))
    self.wait(5)
    self.remove(cap4)

    rudolf = ImageMobject("assets/Rudolf_Diesel.jpg")
    an1892 = Tex("1892").next_to(rudolf, UP)
    self.play(FadeIn(rudolf), Write(an1892))

    self.wait(5)
    self.remove(rudolf, an1892)

    abur = ImageMobject("assets/abur.jpg").scale(1.3)
    self.play(FadeIn(abur))
    self.wait(10)

    self.remove(abur)

    motor = ImageMobject("assets/motor_diesel.jpeg").scale(3)
    an1897 = Tex("1897").next_to(motor, UP)
    self.play(FadeIn(motor), Write(an1897))
    self.wait(4)
    cai = Paragraph("20 de cai", "3 m", "20 tone").next_to(motor, LEFT, buff=1)
    self.play(Write(cai))
    self.wait(4)
    self.remove(an1897, cai, motor)

    naval = ImageMobject("assets/naval.jpg").scale(2)
    self.play(FadeIn(naval))
    self.wait(10)
    self.remove(naval)

    rudolf2 = ImageMobject("assets/Rudolf_Diesel.jpg")

    mort = Tex("1913").next_to(rudolf2, UP)
    self.add(rudolf2)
    self.play(Write(mort))

    self.wait(6)
    self.remove(rudolf2, mort)



def outro(self : Scene):
    pi = SVGMobject("assets/teacher_hooray.svg").move_to(ORIGIN + DOWN)
    pi2 = SVGMobject("assets/teacher_thanks.svg").move_to(pi.get_center())
    thanks = Tex("Va multumim pentru atentie!").to_edge(UP)

    self.add(pi, thanks)
    self.wait(2)
    self.play(ReplacementTransform(pi, pi2))
    self.wait(10)

class ProiectFizica(Scene):
    def construct(self):
        intro_0(self)
        intro(self)
        capitolul1(self)
        capitolul2(self)
        capitolul4(self)
        outro(self)
