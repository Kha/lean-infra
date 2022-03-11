{
  description = "Lean 4 changelog bot";

  outputs = { self, nixpkgs }: {

    packages.x86_64-linux.lean4-nightly-bot =
      with nixpkgs.legacyPackages.x86_64-linux;
      with python3Packages;
      buildPythonApplication {
        name = "lean4-nightly.py";
        propagatedBuildInputs = [ tweepy PyGithub ];
        src = ./.;
      };

    defaultPackage.x86_64-linux = self.packages.x86_64-linux.lean4-nightly-bot;

  };
}
