import langgraph as lg

class LangGraphVisualizer:
    def __init__(self):
        self.graph = lg.Graph()

    def add_step(self, step_name, description):
        self.graph.add_node(step_name, data={"text": description})

    def add_transition(self, from_step, to_step):
        self.graph.add_edge(from_step, to_step)

    def visualize(self, output_file="workflow.html"):
        lg.visualize(self.graph, output_file=output_file)
        print(f"Workflow visualization saved to {output_file}")

# Example usage
visualizer = LangGraphVisualizer()
visualizer.add_step("Start", "Start of the pipeline")
visualizer.add_step("PDF Upload", "Upload PDF to S3")
visualizer.add_transition("Start", "PDF Upload")
visualizer.visualize()
