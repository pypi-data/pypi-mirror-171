from h1st.model.rule_based_model import RuleBasedModel


class BooleanModel(RuleBasedModel):
    """
    In H1st AI, we intend for BooleanModel to mean predictive boolean model. It is somewhat pointless to have a
    "non-predictive" boolean model, since that is basically "just code".
    """

    def execute_rules(self):
        pass
