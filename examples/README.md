# Examples

These examples are synthetic and safe to publish. They show how to use `business-website-skill` without exposing client data.

There are two kinds of examples:

- Public website examples for humans: deployed under `https://business-website-skill.vercel.app/examples/`.
- Brief fixtures for agents: the folders in this directory, used to test the skill workflow.

| Example | Public Website | Agent Fixture |
|---|---|---|
| B2B Service Website | [`/examples/b2b-service/`](https://business-website-skill.vercel.app/examples/b2b-service/) | [`b2b-service/`](./b2b-service/) |
| Industrial Green Tech | [`/examples/industrial-green-tech/`](https://business-website-skill.vercel.app/examples/industrial-green-tech/) | [`industrial-green-tech/`](./industrial-green-tech/) |
| AI SaaS Product | [`/examples/ai-saas-product/`](https://business-website-skill.vercel.app/examples/ai-saas-product/) | [`ai-saas-product/`](./ai-saas-product/) |

Each folder contains:

- `brief.md`: synthetic source material
- `prompt.md`: prompt to run with the skill
- `expected-output.md`: the kind of output the skill should produce

Do not treat these examples as factual company claims. They are pattern examples for testing, demos, and team onboarding.
