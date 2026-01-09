{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Add your project dependencies here
            # Examples:
            # nodejs
            # nodejs.pkgs.pnpm
            # python3
            # go
            # rustc
            # cargo
            # just  # Task runner (if not using system just)
            # git
            # jq
          ];
        };
      }
    );
}
