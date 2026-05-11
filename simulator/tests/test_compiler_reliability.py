from types import SimpleNamespace


def test_semantic_analyzer_handles_missing_optional_nodes():
    import compiler.ast as ast
    from compiler.semantical_errors import SemanticAnalyzer

    analyzer = SemanticAnalyzer(SimpleNamespace(), {}, {}, {})
    void_function = ast.FunctionNode(type=ast.VoidTypeNode(), name="demo")

    while_node = ast.WhileNode(expression=None, sentences=[])
    while_node.set_function(void_function)
    analyzer.visit_while(while_node, None)

    do_while_node = ast.DoWhileNode(expression=None, sentences=[])
    do_while_node.set_function(void_function)
    analyzer.visit_do_while(do_while_node, None)

    for_node = ast.ForNode(assignment=None, condition=None, expression=None, sentences=[])
    for_node.set_function(void_function)
    analyzer.visit_for(for_node, None)

    conditional = ast.ConditionalSentenceNode(condition=None, if_expr=[], else_expr=[])
    conditional.set_function(void_function)
    analyzer.visit_conditional_sentence(conditional, None)

    assignment = ast.AssignmentNode(var=None, expr=None)
    assignment.set_function(void_function)
    analyzer.visit_assignment(assignment, None)

    return_node = ast.ReturnNode(expression=None)
    return_node.set_function(void_function)
    analyzer.visit_return(return_node, None)

    inc_dec = ast.IncDecExpressionNode(var=None, op="++")
    inc_dec.set_function(void_function)
    analyzer.visit_inc_dec_expression(inc_dec, None)

    analyzer.visit_not_expression(ast.NotExpressionNode(expression=None), None)
    analyzer.visit_bit_not_expression(ast.BitNotExpressionNode(expression=None), None)
    analyzer.visit_arithmetic_expression(
        ast.ArithmeticExpressionNode(left=None, op="+", right=None),
        None,
    )
    analyzer.visit_comparision_expression(
        ast.ComparisionExpressionNode(left=None, op="==", right=None),
        None,
    )
    analyzer.visit_boolean_expression(
        ast.BooleanExpressionNode(left=None, op="&&", right=None),
        None,
    )
    analyzer.visit_bitwise_expression(
        ast.BitwiseExpressionNode(left=None, op="&", right=None),
        None,
    )
    analyzer.visit_compound_assignment(
        ast.CompoundAssignmentNode(left=None, op="+=", right=None),
        None,
    )

    assert analyzer._SemanticAnalyzer__get_declaration("missing", None) is None


def test_ast_builder_declaration_preserves_qualifiers():
    import compiler.ast as ast
    from compiler.ast_builder_visitor import ASTBuilderVisitor

    visitor = ASTBuilderVisitor()
    declaration = ast.DeclarationNode(type=ast.IntTypeNode(), var_name="value")
    visitor.visitSimple_declaration = lambda _ctx: declaration

    ctx = SimpleNamespace(
        declaration=lambda: None,
        s_def=object(),
        a_def=None,
        qual=SimpleNamespace(text="const"),
        start=SimpleNamespace(line=3, column=7),
    )

    result = visitor.visitDeclaration(ctx)

    assert result is declaration
    assert result.is_const is True
    assert result.line == 3
    assert result.position == 7


def test_standard_abs_uses_builtin_absolute_value():
    import libraries.standard as standard

    assert standard.abs(-12) == 12
