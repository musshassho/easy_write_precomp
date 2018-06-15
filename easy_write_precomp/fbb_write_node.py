.__author__ Boris Martinez

# assign nuke.createNode() function to a variable for later use.
nuke_create_node = nuke.createNode

def create_my_nodes(node, knobs = "", inpanel = True):
    """
    this function calls nuke_create_node and add a tab and a color picker knob based on the class
    of the node created.
    @param node: Node class.
    @param knobs: Optional string containing a TCL list of name value pairs (like "size 50 quality 19")
    @param inpanel:  Optional boolean to open the control bin (default is True; only applies when the GUI is running).
    @return: result
    """
    result = nuke_create_node(node, knobs, inpanel) # call to nuke_create_node

    if node == "write":
        tab = nuke.Tab_Knob('FBB', 'FBB')
        col = nuke.Color_Knob('PickPos')
        result.addKnob(tab)
        result.addKnob(col)

    return result

# overwrite nuke.createNode
nuke.createNode = create_my_nodes

# KnobChanged callable function

def smart_post_expression():
    """
    This is the function to be called as the first argument for the AddKnobChanged callback later on.
    Sets its context to nuke.thisNode() and picks up the changing knob by the nuke.thisKnob() command.
    @return: None
    """
    n = nuke.thisNode()
    k = nuke.thisKnob()
    if k.name() == "PickPos":
        n['translate'].setExpression('PickPos.r', 0)
        n['translate'].setExpression('PickPos.g', 1)
        n['translate'].setExpression('PickPos.b', 2)
    return None

# adding callbacks to certain node classes.

nuke.addKnobChanged(smart_post_expression, nodeClass="TransformGeo")
nuke.addKnobChanged(smart_post_expression, nodeClass="Sphere")
nuke.addKnobChanged(smart_post_expression, nodeClass="Cube")
nuke.addKnobChanged(smart_post_expression, nodeClass="Card2")
nuke.addKnobChanged(smart_post_expression, nodeClass="Cylinder")
nuke.addKnobChanged(smart_post_expression, nodeClass="Axis2")