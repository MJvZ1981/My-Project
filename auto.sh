function auto() {
  if [ -z "$1" ]; then
    echo "Please provide a commit message"
    return 1
  fi

  # Add all changes
  git add .

  # Commit changes with message provided as argument
  git commit -m "$1"

  # Pull changes from remote repository
  git pull origin main

  # Push changes to remote repository
  git push origin main
}
