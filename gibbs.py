import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Exploring Sampling Strategies based on Gibbs Free Energy and Thermodynamics
    Jarvis Celestial, Arsh Singh

    ## Overview

    In relation to Large Language Models (LLM), certain parameters such as Temperature, Top-$p$, or Top-$k$ are among the most common ways the behavior by which the next token is selected within the probability distribution of tokens. In addition, these parameters are often applied uniformly across the entire response, they are - for all intents and purposes - static. Because of how these parameters affect the variability of the responses, this study aims to model the behavior of token selection with strategies grounded in Thermodynamics, namely the Gibbs-Free Energy (GFE) equation, $G = U + pV - TS$. Because concepts in LLMs map already known variables such as Temperature and Entropy (granted Thermodynamic rather than Informational), we aim to study the efficacy of this model as a means of dynamically controlling the per-token selection process. This helps keep the model stable, creative, responsive to context shifts, and principled on stopping sequences. 
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Understanding the Gibbs-Free Energy Equation

    In Thermodynamics, GFE is a measure of "spontaneity" or how "favorable" certain chemical processes are. $G$ is represented as the amount of energy available within a system that will allow the system to undergo a specific process aimed at achieving a specific desired output. In addition, because of the equilibrious nature of chemical reactions, the direction of $G$ can steer either negative or positive based on the favorability, where highly favorable processes are more negative. For instance, the conversion of Carbon (Graphite) to Carbon (Diamond) is an extremely positive value of $G$, whereas the decomposition of Hydrogen Peroxide into water and Oxygen is a negative value. Knowing this, we can now dive into what each of the variables within the equation mean:

    - $U$: the enthalpy of the system. This simply means the total energy contained within the system, which encompass the potential and kinetic energy of all of the molecules within.
    - $p$: the pressure of a given system
    - $V$: the volume of the system
    - $T$: the temperature of the system
    - $S$: the entropy

    Further down we will explore how these variables will map to concepts in LLM Sampling.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### A brief overview of how LLMs

    The journey of how an input strings fed through an LLM is a very complex one, where they are first sanitized of any special characters and broken apart into Tokens via [Byte Pair Encoding](https://huggingface.co/learn/llm-course/en/chapter6/5). These tokens are then assigned a specific integer value where they are mapped to a high dimension vector wherein each token is related to each other. The embeddings are then passed through a complex neural network called the Transformer. The Transformer is what gives the LLM context when provided with a specific sentence or phrase. Once passed through the transformer, the output of these embeddings are tokens with with logits assigned. Logits are divided using the temperature value in order to scale the probability distribution. Once tokens are distributed according to the temperature, sampling methods are applied in order to determine the next token within the sequence. Most often in platforms such as the [OpenAI Playground](https://platform.openai.com/chat/edit), one can tweak parameters such as Temperature, Top-$k$, and Top-$p$; these are control knobs that modify the selection behavior of the LLM in relation to the next token. Lower values for these factors often lead to determinstic and greedy outcomes, conversely higher values lead to more creative results, but can be susceptible to babbling. 
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
